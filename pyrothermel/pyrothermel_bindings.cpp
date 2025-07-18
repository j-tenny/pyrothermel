//
// Created by john1 on 10/7/2024.
//

#include <pybind11/pybind11.h>
// Include your C++ headers
#include "behaveRun.h"
#include "fuelModels.h"
#include "species_master_table.h"

namespace py = pybind11;


PYBIND11_MODULE(pyrothermel_bindings, m) {

    py::module_ behave_core = m.def_submodule("behave_core", "Unmodified bindings of Behave classes");
    py::module_ units = m.def_submodule("units", "Measurement unit types and conversions");
    py::module_ modes = m.def_submodule("modes", "Calculation modes");

    // Expose enumerations

    // Expose AreaUnitsEnum
    py::class_<AreaUnits> areaUnits(units, "AreaUnits");
    py::enum_<AreaUnits::AreaUnitsEnum>(areaUnits, "AreaUnitsEnum")
            .value("SquareFeet", AreaUnits::SquareFeet)
            .value("Acres", AreaUnits::Acres)
            .value("Hectares", AreaUnits::Hectares)
            .value("SquareMeters", AreaUnits::SquareMeters)
            .value("SquareMiles", AreaUnits::SquareMiles)
            .value("SquareKilometers", AreaUnits::SquareKilometers)
            .export_values();
    areaUnits
            .def_static("toBaseUnits", &AreaUnits::toBaseUnits)
            .def_static("fromBaseUnits", &AreaUnits::fromBaseUnits);

    // Expose BasalAreaUnits struct and enum
    py::class_<BasalAreaUnits> basalAreaUnits(units, "BasalAreaUnits");
    py::enum_<BasalAreaUnits::BasalAreaUnitsEnum>(basalAreaUnits, "BasalAreaUnitsEnum")
            .value("SquareFeetPerAcre", BasalAreaUnits::SquareFeetPerAcre)
            .value("SquareMetersPerHectare", BasalAreaUnits::SquareMetersPerHectare)
            .export_values();
    basalAreaUnits
            .def_static("toBaseUnits", &BasalAreaUnits::toBaseUnits)
            .def_static("fromBaseUnits", &BasalAreaUnits::fromBaseUnits);

    // Expose LengthUnits struct and enum
    py::class_<LengthUnits> lengthUnits(units, "LengthUnits");
    py::enum_<LengthUnits::LengthUnitsEnum>(lengthUnits, "LengthUnitsEnum")
            .value("Feet", LengthUnits::Feet)
            .value("Inches", LengthUnits::Inches)
            .value("Millimeters", LengthUnits::Millimeters)
            .value("Centimeters", LengthUnits::Centimeters)
            .value("Meters", LengthUnits::Meters)
            .value("Chains", LengthUnits::Chains)
            .value("Miles", LengthUnits::Miles)
            .value("Kilometers", LengthUnits::Kilometers)
            .export_values();
    lengthUnits
            .def_static("toBaseUnits", &LengthUnits::toBaseUnits)
            .def_static("fromBaseUnits", &LengthUnits::fromBaseUnits);

    // Expose LoadingUnits struct and enum
    py::class_<LoadingUnits> loadingUnits(units, "LoadingUnits");
    py::enum_<LoadingUnits::LoadingUnitsEnum>(loadingUnits, "LoadingUnitsEnum")
            .value("PoundsPerSquareFoot", LoadingUnits::PoundsPerSquareFoot)
            .value("TonsPerAcre", LoadingUnits::TonsPerAcre)
            .value("TonnesPerHectare", LoadingUnits::TonnesPerHectare)
            .value("KilogramsPerSquareMeter", LoadingUnits::KilogramsPerSquareMeter)
            .export_values();
    loadingUnits
            .def_static("toBaseUnits", &LoadingUnits::toBaseUnits)
            .def_static("fromBaseUnits", &LoadingUnits::fromBaseUnits);

    // Continue similarly for the rest of the structs and enums

    // Expose PressureUnits
    py::class_<PressureUnits> pressureUnits(units, "PressureUnits");
    py::enum_<PressureUnits::PressureUnitsEnum>(pressureUnits, "PressureUnitsEnum")
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
    pressureUnits
            .def_static("toBaseUnits", &PressureUnits::toBaseUnits)
            .def_static("fromBaseUnits", &PressureUnits::fromBaseUnits);

    // Expose SurfaceAreaToVolumeUnits
    py::class_<SurfaceAreaToVolumeUnits> savUnits(units, "SurfaceAreaToVolumeUnits");
    py::enum_<SurfaceAreaToVolumeUnits::SurfaceAreaToVolumeUnitsEnum>(savUnits, "SurfaceAreaToVolumeUnitsEnum")
            .value("SquareFeetOverCubicFeet", SurfaceAreaToVolumeUnits::SquareFeetOverCubicFeet)
            .value("SquareMetersOverCubicMeters", SurfaceAreaToVolumeUnits::SquareMetersOverCubicMeters)
            .value("SquareInchesOverCubicInches", SurfaceAreaToVolumeUnits::SquareInchesOverCubicInches)
            .value("SquareCentimetersOverCubicCentimeters", SurfaceAreaToVolumeUnits::SquareCentimetersOverCubicCentimeters)
            .export_values();
    savUnits
            .def_static("toBaseUnits", &SurfaceAreaToVolumeUnits::toBaseUnits)
            .def_static("fromBaseUnits", &SurfaceAreaToVolumeUnits::fromBaseUnits);

    // Expose SpeedUnits
    py::class_<SpeedUnits> speedUnits(units, "SpeedUnits");
    py::enum_<SpeedUnits::SpeedUnitsEnum>(speedUnits, "SpeedUnitsEnum")
            .value("FeetPerMinute", SpeedUnits::FeetPerMinute)
            .value("ChainsPerHour", SpeedUnits::ChainsPerHour)
            .value("MetersPerSecond", SpeedUnits::MetersPerSecond)
            .value("MetersPerMinute", SpeedUnits::MetersPerMinute)
            .value("MetersPerHour", SpeedUnits::MetersPerHour)
            .value("MilesPerHour", SpeedUnits::MilesPerHour)
            .value("KilometersPerHour", SpeedUnits::KilometersPerHour)
            .export_values();
    speedUnits
            .def_static("toBaseUnits", &SpeedUnits::toBaseUnits)
            .def_static("fromBaseUnits", &SpeedUnits::fromBaseUnits);

    // Expose FractionUnits
    py::class_<FractionUnits> fractionUnits(units, "FractionUnits");
    py::enum_<FractionUnits::FractionUnitsEnum>(fractionUnits, "FractionUnitsEnum")
            .value("Fraction", FractionUnits::Fraction)
            .value("Percent", FractionUnits::Percent)
            .export_values();
    fractionUnits
            .def_static("toBaseUnits", &FractionUnits::toBaseUnits)
            .def_static("fromBaseUnits", &FractionUnits::fromBaseUnits);

    // Expose SlopeUnits
    py::class_<SlopeUnits> slopeUnits(units, "SlopeUnits");
    py::enum_<SlopeUnits::SlopeUnitsEnum>(slopeUnits, "SlopeUnitsEnum")
            .value("Degrees", SlopeUnits::Degrees)
            .value("Percent", SlopeUnits::Percent)
            .export_values();
    slopeUnits
            .def_static("toBaseUnits", &SlopeUnits::toBaseUnits)
            .def_static("fromBaseUnits", &SlopeUnits::fromBaseUnits);

    // Expose DensityUnits
    py::class_<DensityUnits> densityUnits(units, "DensityUnits");
    py::enum_<DensityUnits::DensityUnitsEnum>(densityUnits, "DensityUnitsEnum")
            .value("PoundsPerCubicFoot", DensityUnits::PoundsPerCubicFoot)
            .value("KilogramsPerCubicMeter", DensityUnits::KilogramsPerCubicMeter)
            .export_values();
    densityUnits
            .def_static("toBaseUnits", &DensityUnits::toBaseUnits)
            .def_static("fromBaseUnits", &DensityUnits::fromBaseUnits);

    // Expose HeatOfCombustionUnits
    py::class_<HeatOfCombustionUnits> heatOfCombustionUnits(units, "HeatOfCombustionUnits");
    py::enum_<HeatOfCombustionUnits::HeatOfCombustionUnitsEnum>(heatOfCombustionUnits, "HeatOfCombustionUnitsEnum")
            .value("BtusPerPound", HeatOfCombustionUnits::BtusPerPound)
            .value("KilojoulesPerKilogram", HeatOfCombustionUnits::KilojoulesPerKilogram)
            .export_values();
    heatOfCombustionUnits
            .def_static("toBaseUnits", &HeatOfCombustionUnits::toBaseUnits)
            .def_static("fromBaseUnits", &HeatOfCombustionUnits::fromBaseUnits);

    // Expose HeatSinkUnits
    py::class_<HeatSinkUnits> heatSinkUnits(units, "HeatSinkUnits");
    py::enum_<HeatSinkUnits::HeatSinkUnitsEnum>(heatSinkUnits, "HeatSinkUnitsEnum")
            .value("BtusPerCubicFoot", HeatSinkUnits::BtusPerCubicFoot)
            .value("KilojoulesPerCubicMeter", HeatSinkUnits::KilojoulesPerCubicMeter)
            .export_values();
    heatSinkUnits
            .def_static("toBaseUnits", &HeatSinkUnits::toBaseUnits)
            .def_static("fromBaseUnits", &HeatSinkUnits::fromBaseUnits);

    // Expose HeatPerUnitAreaUnits
    py::class_<HeatPerUnitAreaUnits> hpuaUnits(units, "HeatPerUnitAreaUnits");
    py::enum_<HeatPerUnitAreaUnits::HeatPerUnitAreaUnitsEnum>(hpuaUnits, "HeatPerUnitAreaUnitsEnum")
            .value("BtusPerSquareFoot", HeatPerUnitAreaUnits::BtusPerSquareFoot)
            .value("KilojoulesPerSquareMeter", HeatPerUnitAreaUnits::KilojoulesPerSquareMeter)
            .value("KilowattSecondsPerSquareMeter", HeatPerUnitAreaUnits::KilowattSecondsPerSquareMeter)
            .export_values();
    hpuaUnits
            .def_static("toBaseUnits", &HeatPerUnitAreaUnits::toBaseUnits)
            .def_static("fromBaseUnits", &HeatPerUnitAreaUnits::fromBaseUnits);

    // Expose HeatSourceAndReactionIntensityUnits
    py::class_<HeatSourceAndReactionIntensityUnits> hsriUnits(units, "HeatSourceAndReactionIntensityUnits");
    py::enum_<HeatSourceAndReactionIntensityUnits::HeatSourceAndReactionIntensityUnitsEnum>(hsriUnits, "HeatSourceAndReactionIntensityUnitsEnum")
            .value("BtusPerSquareFootPerMinute", HeatSourceAndReactionIntensityUnits::BtusPerSquareFootPerMinute)
            .value("BtusPerSquareFootPerSecond", HeatSourceAndReactionIntensityUnits::BtusPerSquareFootPerSecond)
            .value("KilojoulesPerSquareMeterPerSecond", HeatSourceAndReactionIntensityUnits::KilojoulesPerSquareMeterPerSecond)
            .value("KilojoulesPerSquareMeterPerMinute", HeatSourceAndReactionIntensityUnits::KilojoulesPerSquareMeterPerMinute)
            .value("KilowattsPerSquareMeter", HeatSourceAndReactionIntensityUnits::KilowattsPerSquareMeter)
            .export_values();
    hsriUnits
            .def_static("toBaseUnits", &HeatSourceAndReactionIntensityUnits::toBaseUnits)
            .def_static("fromBaseUnits", &HeatSourceAndReactionIntensityUnits::fromBaseUnits);

    // Expose FirelineIntensityUnits
    py::class_<FirelineIntensityUnits> firelineIntensityUnits(units, "FirelineIntensityUnits");
    py::enum_<FirelineIntensityUnits::FirelineIntensityUnitsEnum>(firelineIntensityUnits, "FirelineIntensityUnitsEnum")
            .value("BtusPerFootPerSecond", FirelineIntensityUnits::BtusPerFootPerSecond)
            .value("BtusPerFootPerMinute", FirelineIntensityUnits::BtusPerFootPerMinute)
            .value("KilojoulesPerMeterPerSecond", FirelineIntensityUnits::KilojoulesPerMeterPerSecond)
            .value("KilojoulesPerMeterPerMinute", FirelineIntensityUnits::KilojoulesPerMeterPerMinute)
            .value("KilowattsPerMeter", FirelineIntensityUnits::KilowattsPerMeter)
            .export_values();
    firelineIntensityUnits
            .def_static("toBaseUnits", &FirelineIntensityUnits::toBaseUnits)
            .def_static("fromBaseUnits", &FirelineIntensityUnits::fromBaseUnits);

    // Expose TemperatureUnits
    py::class_<TemperatureUnits> temperatureUnits(units, "TemperatureUnits");
    py::enum_<TemperatureUnits::TemperatureUnitsEnum>(temperatureUnits, "TemperatureUnitsEnum")
            .value("Fahrenheit", TemperatureUnits::Fahrenheit)
            .value("Celsius", TemperatureUnits::Celsius)
            .value("Kelvin", TemperatureUnits::Kelvin)
            .export_values();
    temperatureUnits
            .def_static("toBaseUnits", &TemperatureUnits::toBaseUnits)
            .def_static("fromBaseUnits", &TemperatureUnits::fromBaseUnits);

    // Expose TimeUnits
    py::class_<TimeUnits> timeUnits(units, "TimeUnits");
    py::enum_<TimeUnits::TimeUnitsEnum>(timeUnits, "TimeUnitsEnum")
            .value("Minutes", TimeUnits::Minutes)
            .value("Seconds", TimeUnits::Seconds)
            .value("Hours", TimeUnits::Hours)
            .value("Days", TimeUnits::Days)
            .value("Years", TimeUnits::Years)
            .export_values();
    timeUnits
            .def_static("toBaseUnits", &TimeUnits::toBaseUnits)
            .def_static("fromBaseUnits", &TimeUnits::fromBaseUnits);


    py::enum_<MoistureClassInput::MoistureClassInputEnum>(modes, "MoistureClassInput")
            .value("OneHour", MoistureClassInput::OneHour)
            .value("TenHour", MoistureClassInput::TenHour)
            .value("HundredHour", MoistureClassInput::HundredHour)
            .value("LiveHerbaceous", MoistureClassInput::LiveHerbaceous)
            .value("LiveWoody", MoistureClassInput::LiveWoody)
            .value("DeadAggregate", MoistureClassInput::DeadAggregate)
            .value("LiveAggregate", MoistureClassInput::LiveAggregate)
            .export_values();

    // Expose AspenFireSeverityEnum
    py::enum_<AspenFireSeverity::AspenFireSeverityEnum>(modes, "AspenFireSeverity")
            .value("Low", AspenFireSeverity::Low)
            .value("Moderate", AspenFireSeverity::Moderate)
            .export_values();

    // Expose WindAdjustmentFactorShelterMethodEnum
    py::enum_<WindAdjustmentFactorShelterMethod::WindAdjustmentFactorShelterMethodEnum>(modes, "WindAdjustmentFactorShelterMethod")
            .value("Unsheltered", WindAdjustmentFactorShelterMethod::Unsheltered)
            .value("Sheltered", WindAdjustmentFactorShelterMethod::Sheltered)
            .export_values();

    // Expose WindAdjustmentFactorCalculationMethodEnum
    py::enum_<WindAdjustmentFactorCalculationMethod::WindAdjustmentFactorCalculationMethodEnum>(modes, "WindAdjustmentFactorCalculationMethod")
            .value("UserInput", WindAdjustmentFactorCalculationMethod::UserInput)
            .value("UseCrownRatio", WindAdjustmentFactorCalculationMethod::UseCrownRatio)
            .value("DontUseCrownRatio", WindAdjustmentFactorCalculationMethod::DontUseCrownRatio)
            .export_values();

    // Expose WindHeightInputModeEnum
    py::enum_<WindHeightInputMode::WindHeightInputModeEnum>(modes, "WindHeightInputMode")
            .value("DirectMidflame", WindHeightInputMode::DirectMidflame)
            .value("TwentyFoot", WindHeightInputMode::TwentyFoot)
            .value("TenMeter", WindHeightInputMode::TenMeter)
            .export_values();

    // Expose WindAndSpreadOrientationModeEnum
    py::enum_<WindAndSpreadOrientationMode::WindAndSpreadOrientationModeEnum>(modes, "WindAndSpreadOrientationMode")
            .value("RelativeToUpslope", WindAndSpreadOrientationMode::RelativeToUpslope)
            .value("RelativeToNorth", WindAndSpreadOrientationMode::RelativeToNorth)
            .export_values();

    // Expose FuelLifeStateEnum
    py::enum_<FuelLifeState::FuelLifeStateEnum>(modes, "FuelLifeState")
            .value("Dead", FuelLifeState::Dead)
            .value("Live", FuelLifeState::Live)
            .export_values();

    // Expose FuelConstantsEnum
    py::enum_<FuelConstants::FuelConstantsEnum>(modes, "FuelConstants")
            .value("MaxLifeStates", FuelConstants::MaxLifeStates)
            .value("MaxLiveSizeClasses", FuelConstants::MaxLiveSizeClasses)
            .value("MaxDeadSizeClasses", FuelConstants::MaxDeadSizeClasses)
            .value("MaxParticles", FuelConstants::MaxParticles)
            .value("MaxSavrSizeClasses", FuelConstants::MaxSavrSizeClasses)
            .value("MaxFuelModels", FuelConstants::MaxFuelModels)
            .export_values();

    // Expose SurfaceFireSpreadDirectionModeEnum
    py::enum_<SurfaceFireSpreadDirectionMode::SurfaceFireSpreadDirectionModeEnum>(modes, "SurfaceFireSpreadDirectionMode")
            .value("FromIgnitionPoint", SurfaceFireSpreadDirectionMode::FromIgnitionPoint)
            .value("FromPerimeter", SurfaceFireSpreadDirectionMode::FromPerimeter)
            .export_values();

    // Expose TwoFuelModelsMethodEnum
    py::enum_<TwoFuelModelsMethod::TwoFuelModelsMethodEnum>(modes, "TwoFuelModelsMethod")
            .value("NoMethod", TwoFuelModelsMethod::NoMethod)
            .value("Arithmetic", TwoFuelModelsMethod::Arithmetic)
            .value("Harmonic", TwoFuelModelsMethod::Harmonic)
            .value("TwoDimensional", TwoFuelModelsMethod::TwoDimensional)
            .export_values();

    // Expose TwoFuelModelsContantsEnum
    py::enum_<TwoFuelModelsContants::TwoFuelModelsContantsEnum>(modes, "TwoFuelModelsContants")
            .value("First", TwoFuelModelsContants::First)
            .value("Second", TwoFuelModelsContants::Second)
            .value("NumberOfModels", TwoFuelModelsContants::NumberOfModels)
            .export_values();

    // Expose MoistureInputModeEnum
    py::enum_<MoistureInputMode::MoistureInputModeEnum>(modes, "MoistureInputMode")
            .value("BySizeClass", MoistureInputMode::BySizeClass)
            .value("AllAggregate", MoistureInputMode::AllAggregate)
            .value("DeadAggregateAndLiveSizeClass", MoistureInputMode::DeadAggregateAndLiveSizeClass)
            .value("LiveAggregateAndDeadSizeClass", MoistureInputMode::LiveAggregateAndDeadSizeClass)
            .value("MoistureScenario", MoistureInputMode::MoistureScenario)
            .export_values();

    // Expose ChaparralFuelTypeEnum
    py::enum_<ChaparralFuelType::ChaparralFuelTypeEnum>(modes, "ChaparralFuelType")
            .value("NotSet", ChaparralFuelType::NotSet)
            .value("Chamise", ChaparralFuelType::Chamise)
            .value("MixedBrush", ChaparralFuelType::MixedBrush)
            .export_values();

    // Expose ChaparralContantsEnum
    py::enum_<ChaparralContants::ChaparralContantsEnum>(modes, "ChaparralContants")
            .value("NumFuelClasses", ChaparralContants::NumFuelClasses)
            .export_values();

    // Expose ChaparralFuelInputLoadModeEnum
    py::enum_<ChaparralFuelLoadInputMode::ChaparralFuelInputLoadModeEnum>(modes, "ChaparralFuelInputLoadMode")
            .value("DirectFuelLoad", ChaparralFuelLoadInputMode::DirectFuelLoad)
            .value("FuelLoadFromDepthAndChaparralType", ChaparralFuelLoadInputMode::FuelLoadFromDepthAndChaparralType)
            .export_values();


    // Expose FuelModels class
    py::class_<FuelModels>(behave_core, "FuelModels")
            .def(py::init<>())
            .def("setCustomFuelModel", &FuelModels::setCustomFuelModel,
                 py::arg("fuelModelNumber"), py::arg("code"), py::arg("name"),
                 py::arg("fuelBedDepth"), py::arg("lengthUnits"), py::arg("moistureOfExtinctionDead"),
                 py::arg("moistureUnits"), py::arg("heatOfCombustionDead"), py::arg("heatOfCombustionLive"),
                 py::arg("heatOfCombustionUnits"), py::arg("fuelLoadOneHour"), py::arg("fuelLoadTenHour"),
                 py::arg("fuelLoadHundredHour"), py::arg("fuelLoadLiveHerbaceous"), py::arg("fuelLoadLiveWoody"),
                 py::arg("loadingUnits"), py::arg("savrOneHour"), py::arg("savrLiveHerbaceous"),
                 py::arg("savrLiveWoody"), py::arg("savrUnits"), py::arg("isDynamic"))
            .def("getFuelCode", &FuelModels::getFuelCode,
                 py::arg("fuelModelNumber"),
                 "Get the fuel code for the specified fuel model number.")
            .def("getFuelName", &FuelModels::getFuelName,
                 py::arg("fuelModelNumber"),
                 "Get the fuel name for the specified fuel model number.")
            .def("getFuelbedDepth", &FuelModels::getFuelbedDepth,
                 py::arg("fuelModelNumber"),
                 py::arg("lengthUnits"),
                 "Get the fuelbed depth in specified length units.")
            .def("getMoistureOfExtinctionDead", &FuelModels::getMoistureOfExtinctionDead,
                 py::arg("fuelModelNumber"),
                 py::arg("moistureUnits"),
                 "Get the moisture of extinction for dead fuels in specified units.")
            .def("getHeatOfCombustionDead", &FuelModels::getHeatOfCombustionDead,
                 py::arg("fuelModelNumber"),
                 py::arg("heatOfCombustionUnits"),
                 "Get the heat of combustion for dead fuels.")
            .def("getHeatOfCombustionLive", &FuelModels::getHeatOfCombustionLive,
                 py::arg("fuelModelNumber"),
                 py::arg("heatOfCombustionUnits"),
                 "Get the heat of combustion for live fuels.")
            .def("getFuelLoadOneHour", &FuelModels::getFuelLoadOneHour,
                 py::arg("fuelModelNumber"),
                 py::arg("loadingUnits"),
                 "Get the 1-hour fuel load.")
            .def("getFuelLoadTenHour", &FuelModels::getFuelLoadTenHour,
                 py::arg("fuelModelNumber"),
                 py::arg("loadingUnits"),
                 "Get the 10-hour fuel load.")
            .def("getFuelLoadHundredHour", &FuelModels::getFuelLoadHundredHour,
                 py::arg("fuelModelNumber"),
                 py::arg("loadingUnits"),
                 "Get the 100-hour fuel load.")
            .def("getFuelLoadLiveHerbaceous", &FuelModels::getFuelLoadLiveHerbaceous,
                 py::arg("fuelModelNumber"),
                 py::arg("loadingUnits"),
                 "Get the live herbaceous fuel load.")
            .def("getFuelLoadLiveWoody", &FuelModels::getFuelLoadLiveWoody,
                 py::arg("fuelModelNumber"),
                 py::arg("loadingUnits"),
                 "Get the live woody fuel load.")
            .def("getSavrOneHour", &FuelModels::getSavrOneHour,
                 py::arg("fuelModelNumber"),
                 py::arg("savrUnits"),
                 "Get the surface-area-to-volume ratio for 1-hour fuels.")
            .def("getSavrLiveHerbaceous", &FuelModels::getSavrLiveHerbaceous,
                 py::arg("fuelModelNumber"),
                 py::arg("savrUnits"),
                 "Get the surface-area-to-volume ratio for live herbaceous fuels.")
            .def("getSavrLiveWoody", &FuelModels::getSavrLiveWoody,
                 py::arg("fuelModelNumber"),
                 py::arg("savrUnits"),
                 "Get the surface-area-to-volume ratio for live woody fuels.")
            .def("getIsDynamic", &FuelModels::getIsDynamic,
                 py::arg("fuelModelNumber"),
                 "Check if the specified fuel model is dynamic.")
            .def("isFuelModelDefined", &FuelModels::isFuelModelDefined,
                 py::arg("fuelModelNumber"),
                 "Check if the specified fuel model is defined.")
            .def("isFuelModelReserved", &FuelModels::isFuelModelReserved,
                 py::arg("fuelModelNumber"),
                 "Check if the specified fuel model number is reserved.");;

    // Expose SpeciesMasterTable class
    py::class_<SpeciesMasterTable>(behave_core, "SpeciesMasterTable")
            .def(py::init<>());

    // Expose BehaveRun class
    py::class_<BehaveRun>(behave_core, "BehaveRun")
            .def(py::init<FuelModels&, SpeciesMasterTable&>());
//            .def_readwrite("surface", &BehaveRun::surface)
//            .def_readwrite("mortality", &BehaveRun::mortality)
//            .def_readwrite("crown", &BehaveRun::crown)
//            .def_readwrite("contain",&BehaveRun::contain)
//            .def_readwrite("ignite",&BehaveRun::ignite)
//            .def_readwrite("spot",&BehaveRun::spot)
//            .def_readwrite("safety",&BehaveRun::safety);

    // Expose Surface class
    py::class_<Surface>(behave_core, "Surface")
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
    py::class_<Mortality>(behave_core, "Mortality")
            .def("calculateScorchHeight", &Mortality::calculateScorchHeight)
            .def("calculateMortality",&Mortality::calculateMortality);

    // Expose Crown class
    py::class_<Crown>(behave_core, "Crown")
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

