#include "fireSize.h"
#define _USE_MATH_DEFINES
#include <cmath>

FireSize::FireSize()
{

}

FireSize::~FireSize()
{

}

void FireSize::calculateFireBasicDimensions(bool isCrown, double effectiveWindSpeed, SpeedUnits::SpeedUnitsEnum windSpeedRateUnits, double forwardSpreadRate, SpeedUnits::SpeedUnitsEnum spreadRateUnits)
{
    forwardSpreadRate_ = SpeedUnits::toBaseUnits(forwardSpreadRate, spreadRateUnits); // spread rate is now feet per minute
    if (windSpeedRateUnits != SpeedUnits::MilesPerHour)
    {
        effectiveWindSpeed_ = SpeedUnits::toBaseUnits(effectiveWindSpeed, windSpeedRateUnits); // wind speed is now feet per minute
        effectiveWindSpeed_ = SpeedUnits::fromBaseUnits(effectiveWindSpeed_, SpeedUnits::MilesPerHour); // wind speed is now miles per hour
    }
    else
    {
        effectiveWindSpeed_ = effectiveWindSpeed;
    }

    if (isCrown)
    {
        calculateCrownFireLengthToWidthRatio();
    }
    else
    {
        calculateSurfaceFireLengthToWidthRatio();
    }
    
    calculateFireEccentricity();
    calculateBackingSpreadRate();
    calculateFlankingSpreadRate();
    calculateEllipticalDimensions();
}

double FireSize::getFireLengthToWidthRatio() const
{
    return fireLengthToWidthRatio_;
}

double FireSize::getEccentricity() const
{
    return eccentricity_;
}

double FireSize::getBackingSpreadRate(SpeedUnits::SpeedUnitsEnum spreadRateUnits) const
{
    return SpeedUnits::fromBaseUnits(backingSpreadRate_, spreadRateUnits);
}

double FireSize::getFlankingSpreadRate(SpeedUnits::SpeedUnitsEnum spreadRateUnits) const
{
    return SpeedUnits::fromBaseUnits(flankingSpreadRate_, spreadRateUnits);
}

double FireSize::getEllipticalA(LengthUnits::LengthUnitsEnum lengthUnits, double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);
    return LengthUnits::fromBaseUnits((ellipticalA_ * elapsedTime), lengthUnits);
}

double FireSize::getEllipticalB(LengthUnits::LengthUnitsEnum lengthUnits ,double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);
    return  LengthUnits::fromBaseUnits((ellipticalB_ * elapsedTime), lengthUnits);
}

double FireSize::getEllipticalC(LengthUnits::LengthUnitsEnum lengthUnits, double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);
    return LengthUnits::fromBaseUnits((ellipticalC_ * elapsedTime), lengthUnits);
}

double FireSize::getFireLength(LengthUnits::LengthUnitsEnum lengthUnits, double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);
    return LengthUnits::fromBaseUnits((ellipticalB_ * elapsedTime * 2.0), lengthUnits);;
}

double FireSize::getMaxFireWidth(LengthUnits::LengthUnitsEnum lengthUnits, double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);
    return LengthUnits::fromBaseUnits((ellipticalA_ * elapsedTime * 2.0), lengthUnits);;
}

void FireSize::calculateSurfaceFireLengthToWidthRatio()
{
    if (effectiveWindSpeed_ > 1.0e-07)
    {
        fireLengthToWidthRatio_ = .936*exp(.1147*effectiveWindSpeed_)+.461*exp(-.0692*effectiveWindSpeed_)-.397;
        // maximum eccentricity
        if (fireLengthToWidthRatio_ > 8.0)
        {
            fireLengthToWidthRatio_ = 8.0;
        }
    }
    else
    {
        fireLengthToWidthRatio_ = 1.0;
    }
}

void FireSize::calculateCrownFireLengthToWidthRatio()
{
    //Calculates the crown fire length-to-width ratio given the 20-ft wind speed (in mph)
    // (Rothermel 1991, Equation 10, p16)
    double windSpeed = SpeedUnits::fromBaseUnits(effectiveWindSpeed_, SpeedUnits::MilesPerHour);
    if (effectiveWindSpeed_ > 1.0e-07)
    {
        fireLengthToWidthRatio_ = 1.0 + 0.125 * windSpeed;
    }
    else
    {
        fireLengthToWidthRatio_ = 1.0;
    }
}

void FireSize::calculateFireEccentricity()
{
    eccentricity_ = 0.0;
    double x = (fireLengthToWidthRatio_ * fireLengthToWidthRatio_) - 1.0;
    if (x > 0.0)
    {
        eccentricity_ = sqrt(x) / fireLengthToWidthRatio_;
    }
}

void FireSize::calculateEllipticalDimensions()
{
    ellipticalA_ = 0.0;
    ellipticalB_ = 0.0;
    ellipticalC_ = 0.0;
    headingToBackingRatio_ = 0.0;          // Alexander 1985 heading/backing ratio

    double part = 0.0; // Intermediate variable used to calculate Alexandar 1985 ratio
    // Internally A, B, and C are in terms of ft travelled in one minute
    ellipticalB_ = (forwardSpreadRate_ + backingSpreadRate_) / 2.0;
    if (fireLengthToWidthRatio_ > 1e-07)
    {
        part = sqrt(pow(fireLengthToWidthRatio_, 2)-1);
        headingToBackingRatio_ =(fireLengthToWidthRatio_+part)/(fireLengthToWidthRatio_-part);

        ellipticalA_ = ellipticalB_ / fireLengthToWidthRatio_;
    }
    ellipticalC_ = ellipticalB_ - backingSpreadRate_;
}

void FireSize::calculateBackingSpreadRate()
{
    backingSpreadRate_ = forwardSpreadRate_ * (1.0 - eccentricity_) / (1.0 + eccentricity_);
}

void FireSize::calculateFlankingSpreadRate()
{
    const double fireLength = backingSpreadRate_ + forwardSpreadRate_;
    const double width = fireLength / fireLengthToWidthRatio_;
    flankingSpreadRate_ = width * 0.5;
}

double FireSize::getFirePerimeter(bool isCrown, LengthUnits::LengthUnitsEnum lengthUnits, double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    double perimeter = 0;
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);

    if (isCrown)
    {
        // Estimate crown fire perimeter from spread distance and length-to-width ratio as per Rothermel(1991) equation 13 on page 16.
        double spreadDistance = forwardSpreadRate_ * elapsedTime;
        perimeter = 0.5 * M_PI * spreadDistance * (1.0 + 1.0 / fireLengthToWidthRatio_);
    }
    else
    {
        double myEllipticalA = ellipticalA_ * elapsedTime;
        double myEllipticalB = ellipticalB_ * elapsedTime;
        if ((myEllipticalA + myEllipticalB) > 1.0e-07)
        {
            double aMinusB = (myEllipticalA - myEllipticalB);
            double aMinusBSquared = aMinusB * aMinusB;
            double aPlusB = (myEllipticalA + myEllipticalB);
            double aPlusBSquared = aPlusB * aPlusB;
            double h = aMinusBSquared / aPlusBSquared;
            perimeter = M_PI * aPlusB * (1 + (h / 4.0) + ((h * h) / 64.0));
        }
    }
    return LengthUnits::fromBaseUnits(perimeter, lengthUnits);
}

double FireSize::getHeadingToBackingRatio() const
{
    return headingToBackingRatio_;
}

double FireSize::getFireArea(bool isCrown, AreaUnits::AreaUnitsEnum areaUnits, double elapsedTime, TimeUnits::TimeUnitsEnum timeUnits) const
{
    double area = 0.0;
    elapsedTime = TimeUnits::toBaseUnits(elapsedTime, timeUnits);
  
    if (isCrown)
    {
        /* Crown fire area from its forward spread distance and
        * elliptical length - to - width ratio using the assumptions and equations as per
        * Rothermel(1991) equation 11 on page 16 (which ignores backing distance).
        */
        double spreadDistance = forwardSpreadRate_ * elapsedTime;
        area = AreaUnits::fromBaseUnits(M_PI * spreadDistance * spreadDistance / (4.0 * fireLengthToWidthRatio_), areaUnits);
    }
    else
    {
        area = AreaUnits::fromBaseUnits(M_PI * ellipticalA_ * ellipticalB_ * elapsedTime * elapsedTime, areaUnits);
    }
    return area;
}
