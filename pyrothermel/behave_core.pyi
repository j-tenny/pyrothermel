"""
Unmodified bindings of Behave classes
"""
from __future__ import annotations
import pyrothermel.pyrothermel_bindings.modes
import pyrothermel.pyrothermel_bindings.units
__all__ = ['BehaveRun', 'Crown', 'FuelModels', 'Mortality', 'SpeciesMasterTable', 'Surface']
class BehaveRun:
    def __init__(self, arg0: FuelModels, arg1: SpeciesMasterTable) -> None:
        ...
class Crown:
    def doCrownRunRothermel(self) -> None:
        ...
    def doCrownRunScottAndReinhardt(self) -> None:
        ...
    def getActiveRatio(self) -> float:
        ...
    def getCrownFlameLength(self, arg0: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum) -> float:
        ...
    def getFinalFirelineIntensity(self, arg0: pyrothermel.pyrothermel_bindings.units.FirelineIntensityUnits.FirelineIntensityUnitsEnum) -> float:
        ...
    def getFinalFlameLength(self, arg0: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum) -> float:
        ...
    def getFinalSpreadRate(self, arg0: pyrothermel.pyrothermel_bindings.units.SpeedUnits.SpeedUnitsEnum) -> float:
        ...
    def getFireType(self) -> str:
        ...
    def getTransitionRatio(self) -> float:
        ...
    def setUserProvidedWindAdjustmentFactor(self, arg0: float) -> None:
        ...
    def setWindAdjustmentFactorCalculationMethod(self, arg0: pyrothermel.pyrothermel_bindings.modes.WindAdjustmentFactorCalculationMethod) -> None:
        ...
    def updateCrownInputs(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum, arg8: float, arg9: pyrothermel.pyrothermel_bindings.units.SpeedUnits.SpeedUnitsEnum, arg10: pyrothermel.pyrothermel_bindings.modes.WindHeightInputMode, arg11: float, arg12: pyrothermel.pyrothermel_bindings.modes.WindAndSpreadOrientationMode, arg13: float, arg14: pyrothermel.pyrothermel_bindings.units.SlopeUnits.SlopeUnitsEnum, arg15: float, arg16: float, arg17: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum, arg18: float, arg19: float, arg20: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum, arg21: float, arg22: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum, arg23: float, arg24: pyrothermel.pyrothermel_bindings.units.DensityUnits.DensityUnitsEnum) -> None:
        ...
class FuelModels:
    def __init__(self) -> None:
        ...
    def getFuelCode(self, fuelModelNumber: int) -> str:
        """
        Get the fuel code for the specified fuel model number.
        """
    def getFuelLoadHundredHour(self, fuelModelNumber: int, loadingUnits: pyrothermel.pyrothermel_bindings.units.LoadingUnits.LoadingUnitsEnum) -> float:
        """
        Get the 100-hour fuel load.
        """
    def getFuelLoadLiveHerbaceous(self, fuelModelNumber: int, loadingUnits: pyrothermel.pyrothermel_bindings.units.LoadingUnits.LoadingUnitsEnum) -> float:
        """
        Get the live herbaceous fuel load.
        """
    def getFuelLoadLiveWoody(self, fuelModelNumber: int, loadingUnits: pyrothermel.pyrothermel_bindings.units.LoadingUnits.LoadingUnitsEnum) -> float:
        """
        Get the live woody fuel load.
        """
    def getFuelLoadOneHour(self, fuelModelNumber: int, loadingUnits: pyrothermel.pyrothermel_bindings.units.LoadingUnits.LoadingUnitsEnum) -> float:
        """
        Get the 1-hour fuel load.
        """
    def getFuelLoadTenHour(self, fuelModelNumber: int, loadingUnits: pyrothermel.pyrothermel_bindings.units.LoadingUnits.LoadingUnitsEnum) -> float:
        """
        Get the 10-hour fuel load.
        """
    def getFuelName(self, fuelModelNumber: int) -> str:
        """
        Get the fuel name for the specified fuel model number.
        """
    def getFuelbedDepth(self, fuelModelNumber: int, lengthUnits: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum) -> float:
        """
        Get the fuelbed depth in specified length units.
        """
    def getHeatOfCombustionDead(self, fuelModelNumber: int, heatOfCombustionUnits: pyrothermel.pyrothermel_bindings.units.HeatOfCombustionUnits.HeatOfCombustionUnitsEnum) -> float:
        """
        Get the heat of combustion for dead fuels.
        """
    def getHeatOfCombustionLive(self, fuelModelNumber: int, heatOfCombustionUnits: pyrothermel.pyrothermel_bindings.units.HeatOfCombustionUnits.HeatOfCombustionUnitsEnum) -> float:
        """
        Get the heat of combustion for live fuels.
        """
    def getIsDynamic(self, fuelModelNumber: int) -> bool:
        """
        Check if the specified fuel model is dynamic.
        """
    def getMoistureOfExtinctionDead(self, fuelModelNumber: int, moistureUnits: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum) -> float:
        """
        Get the moisture of extinction for dead fuels in specified units.
        """
    def getSavrLiveHerbaceous(self, fuelModelNumber: int, savrUnits: pyrothermel.pyrothermel_bindings.units.SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum) -> float:
        """
        Get the surface-area-to-volume ratio for live herbaceous fuels.
        """
    def getSavrLiveWoody(self, fuelModelNumber: int, savrUnits: pyrothermel.pyrothermel_bindings.units.SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum) -> float:
        """
        Get the surface-area-to-volume ratio for live woody fuels.
        """
    def getSavrOneHour(self, fuelModelNumber: int, savrUnits: pyrothermel.pyrothermel_bindings.units.SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum) -> float:
        """
        Get the surface-area-to-volume ratio for 1-hour fuels.
        """
    def isFuelModelDefined(self, fuelModelNumber: int) -> bool:
        """
        Check if the specified fuel model is defined.
        """
    def isFuelModelReserved(self, fuelModelNumber: int) -> bool:
        """
        Check if the specified fuel model number is reserved.
        """
    def setCustomFuelModel(self, fuelModelNumber: int, code: str, name: str, fuelBedDepth: float, lengthUnits: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum, moistureOfExtinctionDead: float, moistureUnits: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum, heatOfCombustionDead: float, heatOfCombustionLive: float, heatOfCombustionUnits: pyrothermel.pyrothermel_bindings.units.HeatOfCombustionUnits.HeatOfCombustionUnitsEnum, fuelLoadOneHour: float, fuelLoadTenHour: float, fuelLoadHundredHour: float, fuelLoadLiveHerbaceous: float, fuelLoadLiveWoody: float, loadingUnits: pyrothermel.pyrothermel_bindings.units.LoadingUnits.LoadingUnitsEnum, savrOneHour: float, savrLiveHerbaceous: float, savrLiveWoody: float, savrUnits: pyrothermel.pyrothermel_bindings.units.SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum, isDynamic: bool) -> bool:
        ...
class Mortality:
    def calculateMortality(self, arg0: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum) -> float:
        ...
    def calculateScorchHeight(self, arg0: float, arg1: pyrothermel.pyrothermel_bindings.units.FirelineIntensityUnits.FirelineIntensityUnitsEnum, arg2: float, arg3: pyrothermel.pyrothermel_bindings.units.SpeedUnits.SpeedUnitsEnum, arg4: float, arg5: pyrothermel.pyrothermel_bindings.units.TemperatureUnits.TemperatureUnitsEnum, arg6: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum) -> float:
        ...
class SpeciesMasterTable:
    def __init__(self) -> None:
        ...
class Surface:
    def doSurfaceRunInDirectionOfInterest(self, arg0: float, arg1: pyrothermel.pyrothermel_bindings.modes.SurfaceFireSpreadDirectionMode) -> None:
        ...
    def doSurfaceRunInDirectionOfMaxSpread(self) -> None:
        ...
    def getDirectionOfMaxSpread(self) -> float:
        ...
    def getFirelineIntensity(self, arg0: pyrothermel.pyrothermel_bindings.units.FirelineIntensityUnits.FirelineIntensityUnitsEnum) -> float:
        ...
    def getFlameLength(self, arg0: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum) -> float:
        ...
    def getMidflameWindspeed(self, arg0: pyrothermel.pyrothermel_bindings.units.SpeedUnits.SpeedUnitsEnum) -> float:
        ...
    def getSpreadRate(self, arg0: pyrothermel.pyrothermel_bindings.units.SpeedUnits.SpeedUnitsEnum) -> float:
        ...
    def setIsUsingChaparral(self, arg0: bool) -> None:
        ...
    def updateSurfaceInputs(self, arg0: int, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum, arg7: float, arg8: pyrothermel.pyrothermel_bindings.units.SpeedUnits.SpeedUnitsEnum, arg9: pyrothermel.pyrothermel_bindings.modes.WindHeightInputMode, arg10: float, arg11: pyrothermel.pyrothermel_bindings.modes.WindAndSpreadOrientationMode, arg12: float, arg13: pyrothermel.pyrothermel_bindings.units.SlopeUnits.SlopeUnitsEnum, arg14: float, arg15: float, arg16: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum, arg17: float, arg18: pyrothermel.pyrothermel_bindings.units.LengthUnits.LengthUnitsEnum, arg19: float, arg20: pyrothermel.pyrothermel_bindings.units.FractionUnits.FractionUnitsEnum) -> None:
        ...
