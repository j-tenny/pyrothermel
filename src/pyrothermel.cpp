//
// Created by john1 on 10/7/2024.
//

#include <pybind11/pybind11.h>
// Include your C++ headers
#include "behaveRun.h"
#include "fuelModels.h"
#include "species_master_table.h"

namespace py = pybind11;

PYBIND11_MODULE(pyrothermel, m) {
    // Expose enumerations

    // Expose AreaUnitsEnum
    py::enum_<AreaUnits::AreaUnitsEnum>(m, "AreaUnits")
            .value("SquareFeet", AreaUnits::SquareFeet)
            .value("Acres", AreaUnits::Acres)
            .value("Hectares", AreaUnits::Hectares)
            .value("SquareMeters", AreaUnits::SquareMeters)
            .value("SquareMiles", AreaUnits::SquareMiles)
            .value("SquareKilometers", AreaUnits::SquareKilometers)
            .export_values();

    // Expose BasalAreaUnitsEnum
    py::enum_<BasalAreaUnits::BasalAreaUnitsEnum>(m, "BasalAreaUnits")
            .value("SquareFeetPerAcre", BasalAreaUnits::SquareFeetPerAcre)
            .value("SquareMetersPerHectare", BasalAreaUnits::SquareMetersPerHectare)
            .export_values();

    // Expose LengthUnitsEnum
    py::enum_<LengthUnits::LengthUnitsEnum>(m, "LengthUnits")
            .value("Feet", LengthUnits::Feet)
            .value("Inches", LengthUnits::Inches)
            .value("Millimeters", LengthUnits::Millimeters)
            .value("Centimeters", LengthUnits::Centimeters)
            .value("Meters", LengthUnits::Meters)
            .value("Chains", LengthUnits::Chains)
            .value("Miles", LengthUnits::Miles)
            .value("Kilometers", LengthUnits::Kilometers)
            .export_values();

    // Expose LoadingUnitsEnum
    py::enum_<LoadingUnits::LoadingUnitsEnum>(m, "LoadingUnits")
            .value("PoundsPerSquareFoot", LoadingUnits::PoundsPerSquareFoot)
            .value("TonsPerAcre", LoadingUnits::TonsPerAcre)
            .value("TonnesPerHectare", LoadingUnits::TonnesPerHectare)
            .value("KilogramsPerSquareMeter", LoadingUnits::KilogramsPerSquareMeter)
            .export_values();

    // Continue similarly for the rest of the enums

    // Expose PressureUnitsEnum
    py::enum_<PressureUnits::PressureUnitsEnum>(m, "PressureUnits")
            .value("Pascal", PressureUnits::Pascal)
            .value("HectoPascal", PressureUnits::HectoPascal)
            .value("KiloPascal", PressureUnits::KiloPascal)
            .value("MegaPascal", PressureUnits::MegaPascal)
            .value("GigaPascal", PressureUnits::GigaPascal)
            .value("Bar", PressureUnits::Bar)
            .value("Atmosphere", PressureUnits::Atmosphere)
            .value("TechnicalAtmosphere", PressureUnits::TechnicalAtmosphere)
            .value("PoundPerSquareInch", PressureUnits::PoundPerSquareInch)
            .export_values();

    // Expose SurfaceAreaToVolumeUnitsEnum
    py::enum_<SurfaceAreaToVolumeUnits::SurfaceAreaToVolumeUnitsEnum>(m, "SurfaceAreaToVolumeUnits")
            .value("SquareFeetOverCubicFeet", SurfaceAreaToVolumeUnits::SquareFeetOverCubicFeet)
            .value("SquareMetersOverCubicMeters", SurfaceAreaToVolumeUnits::SquareMetersOverCubicMeters)
            .value("SquareInchesOverCubicInches", SurfaceAreaToVolumeUnits::SquareInchesOverCubicInches)
            .value("SquareCentimetersOverCubicCentimeters", SurfaceAreaToVolumeUnits::SquareCentimetersOverCubicCentimeters)
            .export_values();

    // Expose SpeedUnitsEnum
    py::enum_<SpeedUnits::SpeedUnitsEnum>(m, "SpeedUnits")
            .value("FeetPerMinute", SpeedUnits::FeetPerMinute)
            .value("ChainsPerHour", SpeedUnits::ChainsPerHour)
            .value("MetersPerSecond", SpeedUnits::MetersPerSecond)
            .value("MetersPerMinute", SpeedUnits::MetersPerMinute)
            .value("MetersPerHour", SpeedUnits::MetersPerHour)
            .value("MilesPerHour", SpeedUnits::MilesPerHour)
            .value("KilometersPerHour", SpeedUnits::KilometersPerHour)
            .export_values();

    // Expose FractionUnitsEnum
    py::enum_<FractionUnits::FractionUnitsEnum>(m, "FractionUnits")
            .value("Fraction", FractionUnits::Fraction)
            .value("Percent", FractionUnits::Percent)
            .export_values();

    // Expose SlopeUnitsEnum
    py::enum_<SlopeUnits::SlopeUnitsEnum>(m, "SlopeUnits")
            .value("Degrees", SlopeUnits::Degrees)
            .value("Percent", SlopeUnits::Percent)
            .export_values();

    // Expose DensityUnitsEnum
    py::enum_<DensityUnits::DensityUnitsEnum>(m, "DensityUnits")
            .value("PoundsPerCubicFoot", DensityUnits::PoundsPerCubicFoot)
            .value("KilogramsPerCubicMeter", DensityUnits::KilogramsPerCubicMeter)
            .export_values();

    // Expose HeatOfCombustionUnitsEnum
    py::enum_<HeatOfCombustionUnits::HeatOfCombustionUnitsEnum>(m, "HeatOfCombustionUnits")
            .value("BtusPerPound", HeatOfCombustionUnits::BtusPerPound)
            .value("KilojoulesPerKilogram", HeatOfCombustionUnits::KilojoulesPerKilogram)
            .export_values();

    // Expose HeatSinkUnitsEnum
    py::enum_<HeatSinkUnits::HeatSinkUnitsEnum>(m, "HeatSinkUnits")
            .value("BtusPerCubicFoot", HeatSinkUnits::BtusPerCubicFoot)
            .value("KilojoulesPerCubicMeter", HeatSinkUnits::KilojoulesPerCubicMeter)
            .export_values();

    // Expose HeatPerUnitAreaUnitsEnum
    py::enum_<HeatPerUnitAreaUnits::HeatPerUnitAreaUnitsEnum>(m, "HeatPerUnitAreaUnits")
            .value("BtusPerSquareFoot", HeatPerUnitAreaUnits::BtusPerSquareFoot)
            .value("KilojoulesPerSquareMeter", HeatPerUnitAreaUnits::KilojoulesPerSquareMeter)
            .value("KilowattSecondsPerSquareMeter", HeatPerUnitAreaUnits::KilowattSecondsPerSquareMeter)
            .export_values();

    // Expose HeatSourceAndReactionIntensityUnitsEnum
    py::enum_<HeatSourceAndReactionIntensityUnits::HeatSourceAndReactionIntensityUnitsEnum>(m, "HeatSourceAndReactionIntensityUnits")
            .value("BtusPerSquareFootPerMinute", HeatSourceAndReactionIntensityUnits::BtusPerSquareFootPerMinute)
            .value("BtusPerSquareFootPerSecond", HeatSourceAndReactionIntensityUnits::BtusPerSquareFootPerSecond)
            .value("KilojoulesPerSquareMeterPerSecond", HeatSourceAndReactionIntensityUnits::KilojoulesPerSquareMeterPerSecond)
            .value("KilojoulesPerSquareMeterPerMinute", HeatSourceAndReactionIntensityUnits::KilojoulesPerSquareMeterPerMinute)
            .value("KilowattsPerSquareMeter", HeatSourceAndReactionIntensityUnits::KilowattsPerSquareMeter)
            .export_values();

    // Expose FirelineIntensityUnitsEnum
    py::enum_<FirelineIntensityUnits::FirelineIntensityUnitsEnum>(m, "FirelineIntensityUnits")
            .value("BtusPerFootPerSecond", FirelineIntensityUnits::BtusPerFootPerSecond)
            .value("BtusPerFootPerMinute", FirelineIntensityUnits::BtusPerFootPerMinute)
            .value("KilojoulesPerMeterPerSecond", FirelineIntensityUnits::KilojoulesPerMeterPerSecond)
            .value("KilojoulesPerMeterPerMinute", FirelineIntensityUnits::KilojoulesPerMeterPerMinute)
            .value("KilowattsPerMeter", FirelineIntensityUnits::KilowattsPerMeter)
            .export_values();

    // Expose TemperatureUnitsEnum
    py::enum_<TemperatureUnits::TemperatureUnitsEnum>(m, "TemperatureUnits")
            .value("Fahrenheit", TemperatureUnits::Fahrenheit)
            .value("Celsius", TemperatureUnits::Celsius)
            .value("Kelvin", TemperatureUnits::Kelvin)
            .export_values();

    // Expose TimeUnitsEnum
    py::enum_<TimeUnits::TimeUnitsEnum>(m, "TimeUnits")
            .value("Minutes", TimeUnits::Minutes)
            .value("Seconds", TimeUnits::Seconds)
            .value("Hours", TimeUnits::Hours)
            .value("Days", TimeUnits::Days)
            .value("Years", TimeUnits::Years)
            .export_values();

    py::enum_<MoistureClassInput::MoistureClassInputEnum>(m, "MoistureClassInput")
            .value("OneHour", MoistureClassInput::OneHour)
            .value("TenHour", MoistureClassInput::TenHour)
            .value("HundredHour", MoistureClassInput::HundredHour)
            .value("LiveHerbaceous", MoistureClassInput::LiveHerbaceous)
            .value("LiveWoody", MoistureClassInput::LiveWoody)
            .value("DeadAggregate", MoistureClassInput::DeadAggregate)
            .value("LiveAggregate", MoistureClassInput::LiveAggregate)
            .export_values();

    // Expose AspenFireSeverityEnum
    py::enum_<AspenFireSeverity::AspenFireSeverityEnum>(m, "AspenFireSeverity")
            .value("Low", AspenFireSeverity::Low)
            .value("Moderate", AspenFireSeverity::Moderate)
            .export_values();

    // Expose WindAdjustmentFactorShelterMethodEnum
    py::enum_<WindAdjustmentFactorShelterMethod::WindAdjustmentFactorShelterMethodEnum>(m, "WindAdjustmentFactorShelterMethod")
            .value("Unsheltered", WindAdjustmentFactorShelterMethod::Unsheltered)
            .value("Sheltered", WindAdjustmentFactorShelterMethod::Sheltered)
            .export_values();

    // Expose WindAdjustmentFactorCalculationMethodEnum
    py::enum_<WindAdjustmentFactorCalculationMethod::WindAdjustmentFactorCalculationMethodEnum>(m, "WindAdjustmentFactorCalculationMethod")
            .value("UserInput", WindAdjustmentFactorCalculationMethod::UserInput)
            .value("UseCrownRatio", WindAdjustmentFactorCalculationMethod::UseCrownRatio)
            .value("DontUseCrownRatio", WindAdjustmentFactorCalculationMethod::DontUseCrownRatio)
            .export_values();

    // Expose WindHeightInputModeEnum
    py::enum_<WindHeightInputMode::WindHeightInputModeEnum>(m, "WindHeightInputMode")
            .value("DirectMidflame", WindHeightInputMode::DirectMidflame)
            .value("TwentyFoot", WindHeightInputMode::TwentyFoot)
            .value("TenMeter", WindHeightInputMode::TenMeter)
            .export_values();

    // Expose WindAndSpreadOrientationModeEnum
    py::enum_<WindAndSpreadOrientationMode::WindAndSpreadOrientationModeEnum>(m, "WindAndSpreadOrientationMode")
            .value("RelativeToUpslope", WindAndSpreadOrientationMode::RelativeToUpslope)
            .value("RelativeToNorth", WindAndSpreadOrientationMode::RelativeToNorth)
            .export_values();

    // Expose FuelLifeStateEnum
    py::enum_<FuelLifeState::FuelLifeStateEnum>(m, "FuelLifeState")
            .value("Dead", FuelLifeState::Dead)
            .value("Live", FuelLifeState::Live)
            .export_values();

    // Expose FuelConstantsEnum
    py::enum_<FuelConstants::FuelConstantsEnum>(m, "FuelConstants")
            .value("MaxLifeStates", FuelConstants::MaxLifeStates)
            .value("MaxLiveSizeClasses", FuelConstants::MaxLiveSizeClasses)
            .value("MaxDeadSizeClasses", FuelConstants::MaxDeadSizeClasses)
            .value("MaxParticles", FuelConstants::MaxParticles)
            .value("MaxSavrSizeClasses", FuelConstants::MaxSavrSizeClasses)
            .value("MaxFuelModels", FuelConstants::MaxFuelModels)
            .export_values();

    // Expose SurfaceFireSpreadDirectionModeEnum
    py::enum_<SurfaceFireSpreadDirectionMode::SurfaceFireSpreadDirectionModeEnum>(m, "SurfaceFireSpreadDirectionMode")
            .value("FromIgnitionPoint", SurfaceFireSpreadDirectionMode::FromIgnitionPoint)
            .value("FromPerimeter", SurfaceFireSpreadDirectionMode::FromPerimeter)
            .export_values();

    // Expose TwoFuelModelsMethodEnum
    py::enum_<TwoFuelModelsMethod::TwoFuelModelsMethodEnum>(m, "TwoFuelModelsMethod")
            .value("NoMethod", TwoFuelModelsMethod::NoMethod)
            .value("Arithmetic", TwoFuelModelsMethod::Arithmetic)
            .value("Harmonic", TwoFuelModelsMethod::Harmonic)
            .value("TwoDimensional", TwoFuelModelsMethod::TwoDimensional)
            .export_values();

    // Expose TwoFuelModelsContantsEnum
    py::enum_<TwoFuelModelsContants::TwoFuelModelsContantsEnum>(m, "TwoFuelModelsContants")
            .value("First", TwoFuelModelsContants::First)
            .value("Second", TwoFuelModelsContants::Second)
            .value("NumberOfModels", TwoFuelModelsContants::NumberOfModels)
            .export_values();

    // Expose MoistureInputModeEnum
    py::enum_<MoistureInputMode::MoistureInputModeEnum>(m, "MoistureInputMode")
            .value("BySizeClass", MoistureInputMode::BySizeClass)
            .value("AllAggregate", MoistureInputMode::AllAggregate)
            .value("DeadAggregateAndLiveSizeClass", MoistureInputMode::DeadAggregateAndLiveSizeClass)
            .value("LiveAggregateAndDeadSizeClass", MoistureInputMode::LiveAggregateAndDeadSizeClass)
            .value("MoistureScenario", MoistureInputMode::MoistureScenario)
            .export_values();

    // Expose ChaparralFuelTypeEnum
    py::enum_<ChaparralFuelType::ChaparralFuelTypeEnum>(m, "ChaparralFuelType")
            .value("NotSet", ChaparralFuelType::NotSet)
            .value("Chamise", ChaparralFuelType::Chamise)
            .value("MixedBrush", ChaparralFuelType::MixedBrush)
            .export_values();

    // Expose ChaparralContantsEnum
    py::enum_<ChaparralContants::ChaparralContantsEnum>(m, "ChaparralContants")
            .value("NumFuelClasses", ChaparralContants::NumFuelClasses)
            .export_values();

    // Expose ChaparralFuelInputLoadModeEnum
    py::enum_<ChaparralFuelLoadInputMode::ChaparralFuelInputLoadModeEnum>(m, "ChaparralFuelInputLoadMode")
            .value("DirectFuelLoad", ChaparralFuelLoadInputMode::DirectFuelLoad)
            .value("FuelLoadFromDepthAndChaparralType", ChaparralFuelLoadInputMode::FuelLoadFromDepthAndChaparralType)
            .export_values();


    // Expose FuelModels class
    py::class_<FuelModels>(m, "FuelModels")
            .def(py::init<>())
            .def("setCustomFuelModel", &FuelModels::setCustomFuelModel,
                 py::arg("fuelModelNumber"), py::arg("code"), py::arg("name"),
                 py::arg("fuelBedDepth"), py::arg("lengthUnits"), py::arg("moistureOfExtinctionDead"),
                 py::arg("moistureUnits"), py::arg("heatOfCombustionDead"), py::arg("heatOfCombustionLive"),
                 py::arg("heatOfCombustionUnits"), py::arg("fuelLoadOneHour"), py::arg("fuelLoadTenHour"),
                 py::arg("fuelLoadHundredHour"), py::arg("fuelLoadLiveHerbaceous"), py::arg("fuelLoadLiveWoody"),
                 py::arg("loadingUnits"), py::arg("savrOneHour"), py::arg("savrLiveHerbaceous"),
                 py::arg("savrLiveWoody"), py::arg("savrUnits"), py::arg("isDynamic"));

    // Expose SpeciesMasterTable class
    py::class_<SpeciesMasterTable>(m, "SpeciesMasterTable")
            .def(py::init<>());

    // Expose BehaveRun class
    py::class_<BehaveRun>(m, "BehaveRun")
            .def(py::init<FuelModels&, SpeciesMasterTable&>())
            .def_readwrite("surface", &BehaveRun::surface)
            .def_readwrite("mortality", &BehaveRun::mortality)
            .def_readwrite("crown", &BehaveRun::crown)
            .def_readwrite("contain",&BehaveRun::contain)
            .def_readwrite("ignite",&BehaveRun::ignite)
            .def_readwrite("spot",&BehaveRun::spot)
            .def_readwrite("safety",&BehaveRun::safety);

    // Expose Surface class
    py::class_<Surface>(m, "Surface")
            .def("updateSurfaceInputs", &Surface::updateSurfaceInputs)
            .def("doSurfaceRunInDirectionOfMaxSpread", &Surface::doSurfaceRunInDirectionOfMaxSpread)
            .def("doSurfaceRunInDirectionOfInterest",&Surface::doSurfaceRunInDirectionOfInterest)
            .def("getMidflameWindspeed",&Surface::getMidflameWindspeed)
            .def("getSpreadRate", &Surface::getSpreadRate)
            .def("getFlameLength", &Surface::getFlameLength)
            .def("getDirectionOfMaxSpread", &Surface::getDirectionOfMaxSpread)
            .def("setIsUsingChaparral", &Surface::setIsUsingChaparral)
            .def("getFirelineIntensity",&Surface::getFirelineIntensity);

    // Expose Mortality class
    py::class_<Mortality>(m, "Mortality")
            .def("calculateScorchHeight", &Mortality::calculateScorchHeight)
            .def("calculateMortality",&Mortality::calculateMortality);

    // Expose Crown class
    py::class_<Crown>(m, "Crown")
            .def("setWindAdjustmentFactorCalculationMethod", &Crown::setWindAdjustmentFactorCalculationMethod)
            .def("setUserProvidedWindAdjustmentFactor", &Crown::setUserProvidedWindAdjustmentFactor)
            .def("updateCrownInputs", &Crown::updateCrownInputs)
            .def("doCrownRunRothermel", &Crown::doCrownRunRothermel)
            .def("doCrownRunScottAndReinhardt", &Crown::doCrownRunScottAndReinhardt)
            .def("getFinalSpreadRate", &Crown::getFinalSpreadRate)
            .def("getFinalFirelineIntensity", &Crown::getFinalFirelineIntesity)
            .def("getFinalFlameLength", &Crown::getFinalFlameLength)
            .def("getCrownFlameLength", &Crown::getCrownFlameLength)
            .def("getTransitionRatio", &Crown::getTransitionRatio)
            .def("getActiveRatio", &Crown::getActiveRatio)
            .def("getFireType", &Crown::getFireTypeStr);

    // TODO: Expose other necessary classes and methods
}

