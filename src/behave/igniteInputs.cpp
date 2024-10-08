#include "igniteInputs.h"

IgniteInputs::IgniteInputs()
{
    moistureOneHour_ = 0.0;
    moistureHundredHour_ = 0.0;
    airTemperature_ = 0.0;
    sunShade_ = 0.0;
    fuelBedType_ = IgnitionFuelBedType::PonderosaPineLitter;
    duffDepth_ = 0.0;
  
    lightningChargeType_ = LightningCharge::Unknown;
}

IgniteInputs::~IgniteInputs()
{

}

void IgniteInputs::initializeMembers()
{
    moistureOneHour_ = 0.0;
    moistureHundredHour_ = 0.0;
    airTemperature_ = 0.0;
    sunShade_ = 0.0;
    fuelBedType_ = IgnitionFuelBedType::PonderosaPineLitter;
    duffDepth_ = 0.0;

    lightningChargeType_ = LightningCharge::Unknown;
}

void IgniteInputs::updateIgniteInputs(double moistureOneHour, double moistureHundredHour, FractionUnits::FractionUnitsEnum moistureUnits,
    double airTemperature, TemperatureUnits::TemperatureUnitsEnum temperatureUnits, double sunShade, FractionUnits::FractionUnitsEnum sunShadeUnits,
    IgnitionFuelBedType::IgnitionFuelBedTypeEnum fuelBedType, double duffDepth, LengthUnits::LengthUnitsEnum duffDepthUnits,
    LightningCharge::LightningChargeEnum lightningChargeType)
{
    setMoistureOneHour(moistureOneHour, moistureUnits);
    setMoistureHundredHour(moistureHundredHour, moistureUnits);
    setAirTemperature(airTemperature, temperatureUnits);
    setSunShade(sunShade, sunShadeUnits);
    fuelBedType_ = fuelBedType;
    setDuffDepth(duffDepth, duffDepthUnits);
    lightningChargeType_ = lightningChargeType;
}

void IgniteInputs::setMoistureOneHour(double moistureOneHour, FractionUnits::FractionUnitsEnum moistureUnits)
{
    moistureOneHour_ = FractionUnits::toBaseUnits(moistureOneHour, moistureUnits);
}

void IgniteInputs::setMoistureHundredHour(double moistureHundredHour, FractionUnits::FractionUnitsEnum moistureUnits)
{
    moistureHundredHour_ = FractionUnits::toBaseUnits(moistureHundredHour, moistureUnits);
}

void IgniteInputs::setAirTemperature(double airTemperature, TemperatureUnits::TemperatureUnitsEnum temperatureUnits)
{
    airTemperature_ = TemperatureUnits::toBaseUnits(airTemperature, temperatureUnits);
}

void IgniteInputs::setSunShade(double sunShade, FractionUnits::FractionUnitsEnum sunShadeUnits)
{
    sunShade_ = FractionUnits::toBaseUnits(sunShade, sunShadeUnits);
}

void IgniteInputs::setIgnitionFuelBedType(IgnitionFuelBedType::IgnitionFuelBedTypeEnum fuelBedType)
{
    fuelBedType_ = fuelBedType;
}

void IgniteInputs::setDuffDepth(double duffDepth, LengthUnits::LengthUnitsEnum lengthUnits)
{
    duffDepth_ = LengthUnits::toBaseUnits(duffDepth, lengthUnits);
}

void IgniteInputs::setLightningChargeType(LightningCharge::LightningChargeEnum lightningChargeType)
{
    lightningChargeType_ = lightningChargeType;
}

double IgniteInputs::getAirTemperature(TemperatureUnits::TemperatureUnitsEnum desiredUnits)
{
    return TemperatureUnits::fromBaseUnits(airTemperature_, desiredUnits);
}

double IgniteInputs::getMoistureOneHour(FractionUnits::FractionUnitsEnum desiredUnits)
{
    return FractionUnits::fromBaseUnits(moistureOneHour_, desiredUnits);
}

double IgniteInputs::getMoistureHundredHour(FractionUnits::FractionUnitsEnum desiredUnits)
{
    return FractionUnits::fromBaseUnits(moistureHundredHour_, desiredUnits);
}

double IgniteInputs::getSunShade(FractionUnits::FractionUnitsEnum desiredUnits)
{
    return FractionUnits::fromBaseUnits(sunShade_, desiredUnits);
}

IgnitionFuelBedType::IgnitionFuelBedTypeEnum IgniteInputs::getIgnitionFuelBedType()
{
    return fuelBedType_;
}

double IgniteInputs::getDuffDepth(LengthUnits::LengthUnitsEnum desiredUnits)
{
    return LengthUnits::fromBaseUnits(duffDepth_,desiredUnits);
}

LightningCharge::LightningChargeEnum IgniteInputs::getLightningChargeType()
{
    return lightningChargeType_;
}
