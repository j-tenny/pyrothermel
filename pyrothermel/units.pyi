"""
Measurement unit types and conversions
"""
from __future__ import annotations
import typing
__all__ = ['AreaUnits', 'BasalAreaUnits', 'DensityUnits', 'FirelineIntensityUnits', 'FractionUnits', 'HeatOfCombustionUnits', 'HeatPerUnitAreaUnits', 'HeatSinkUnits', 'HeatSourceAndReactionIntensityUnits', 'LengthUnits', 'LoadingUnits', 'PressureUnits', 'SlopeUnits', 'SpeedUnits', 'SurfaceAreaToVolumeUnits', 'TemperatureUnits', 'TimeUnits']
class AreaUnits:
    class AreaUnitsEnum:
        """
        Members:
        
          SquareFeet
        
          Acres
        
          Hectares
        
          SquareMeters
        
          SquareMiles
        
          SquareKilometers
        """
        Acres: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.Acres: 1>
        Hectares: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.Hectares: 2>
        SquareFeet: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareFeet: 0>
        SquareKilometers: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareKilometers: 5>
        SquareMeters: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareMeters: 3>
        SquareMiles: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareMiles: 4>
        __members__: typing.ClassVar[dict[str, AreaUnits.AreaUnitsEnum]]  # value = {'SquareFeet': <AreaUnitsEnum.SquareFeet: 0>, 'Acres': <AreaUnitsEnum.Acres: 1>, 'Hectares': <AreaUnitsEnum.Hectares: 2>, 'SquareMeters': <AreaUnitsEnum.SquareMeters: 3>, 'SquareMiles': <AreaUnitsEnum.SquareMiles: 4>, 'SquareKilometers': <AreaUnitsEnum.SquareKilometers: 5>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Acres: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.Acres: 1>
    Hectares: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.Hectares: 2>
    SquareFeet: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareFeet: 0>
    SquareKilometers: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareKilometers: 5>
    SquareMeters: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareMeters: 3>
    SquareMiles: typing.ClassVar[AreaUnits.AreaUnitsEnum]  # value = <AreaUnitsEnum.SquareMiles: 4>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: AreaUnits.AreaUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: AreaUnits.AreaUnitsEnum) -> float:
        ...
class BasalAreaUnits:
    class BasalAreaUnitsEnum:
        """
        Members:
        
          SquareFeetPerAcre
        
          SquareMetersPerHectare
        """
        SquareFeetPerAcre: typing.ClassVar[BasalAreaUnits.BasalAreaUnitsEnum]  # value = <BasalAreaUnitsEnum.SquareFeetPerAcre: 0>
        SquareMetersPerHectare: typing.ClassVar[BasalAreaUnits.BasalAreaUnitsEnum]  # value = <BasalAreaUnitsEnum.SquareMetersPerHectare: 1>
        __members__: typing.ClassVar[dict[str, BasalAreaUnits.BasalAreaUnitsEnum]]  # value = {'SquareFeetPerAcre': <BasalAreaUnitsEnum.SquareFeetPerAcre: 0>, 'SquareMetersPerHectare': <BasalAreaUnitsEnum.SquareMetersPerHectare: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    SquareFeetPerAcre: typing.ClassVar[BasalAreaUnits.BasalAreaUnitsEnum]  # value = <BasalAreaUnitsEnum.SquareFeetPerAcre: 0>
    SquareMetersPerHectare: typing.ClassVar[BasalAreaUnits.BasalAreaUnitsEnum]  # value = <BasalAreaUnitsEnum.SquareMetersPerHectare: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: BasalAreaUnits.BasalAreaUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: BasalAreaUnits.BasalAreaUnitsEnum) -> float:
        ...
class DensityUnits:
    class DensityUnitsEnum:
        """
        Members:
        
          PoundsPerCubicFoot
        
          KilogramsPerCubicMeter
        """
        KilogramsPerCubicMeter: typing.ClassVar[DensityUnits.DensityUnitsEnum]  # value = <DensityUnitsEnum.KilogramsPerCubicMeter: 1>
        PoundsPerCubicFoot: typing.ClassVar[DensityUnits.DensityUnitsEnum]  # value = <DensityUnitsEnum.PoundsPerCubicFoot: 0>
        __members__: typing.ClassVar[dict[str, DensityUnits.DensityUnitsEnum]]  # value = {'PoundsPerCubicFoot': <DensityUnitsEnum.PoundsPerCubicFoot: 0>, 'KilogramsPerCubicMeter': <DensityUnitsEnum.KilogramsPerCubicMeter: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    KilogramsPerCubicMeter: typing.ClassVar[DensityUnits.DensityUnitsEnum]  # value = <DensityUnitsEnum.KilogramsPerCubicMeter: 1>
    PoundsPerCubicFoot: typing.ClassVar[DensityUnits.DensityUnitsEnum]  # value = <DensityUnitsEnum.PoundsPerCubicFoot: 0>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: DensityUnits.DensityUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: DensityUnits.DensityUnitsEnum) -> float:
        ...
class FirelineIntensityUnits:
    class FirelineIntensityUnitsEnum:
        """
        Members:
        
          BtusPerFootPerSecond
        
          BtusPerFootPerMinute
        
          KilojoulesPerMeterPerSecond
        
          KilojoulesPerMeterPerMinute
        
          KilowattsPerMeter
        """
        BtusPerFootPerMinute: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.BtusPerFootPerMinute: 1>
        BtusPerFootPerSecond: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.BtusPerFootPerSecond: 0>
        KilojoulesPerMeterPerMinute: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.KilojoulesPerMeterPerMinute: 3>
        KilojoulesPerMeterPerSecond: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.KilojoulesPerMeterPerSecond: 2>
        KilowattsPerMeter: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.KilowattsPerMeter: 4>
        __members__: typing.ClassVar[dict[str, FirelineIntensityUnits.FirelineIntensityUnitsEnum]]  # value = {'BtusPerFootPerSecond': <FirelineIntensityUnitsEnum.BtusPerFootPerSecond: 0>, 'BtusPerFootPerMinute': <FirelineIntensityUnitsEnum.BtusPerFootPerMinute: 1>, 'KilojoulesPerMeterPerSecond': <FirelineIntensityUnitsEnum.KilojoulesPerMeterPerSecond: 2>, 'KilojoulesPerMeterPerMinute': <FirelineIntensityUnitsEnum.KilojoulesPerMeterPerMinute: 3>, 'KilowattsPerMeter': <FirelineIntensityUnitsEnum.KilowattsPerMeter: 4>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    BtusPerFootPerMinute: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.BtusPerFootPerMinute: 1>
    BtusPerFootPerSecond: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.BtusPerFootPerSecond: 0>
    KilojoulesPerMeterPerMinute: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.KilojoulesPerMeterPerMinute: 3>
    KilojoulesPerMeterPerSecond: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.KilojoulesPerMeterPerSecond: 2>
    KilowattsPerMeter: typing.ClassVar[FirelineIntensityUnits.FirelineIntensityUnitsEnum]  # value = <FirelineIntensityUnitsEnum.KilowattsPerMeter: 4>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: FirelineIntensityUnits.FirelineIntensityUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: FirelineIntensityUnits.FirelineIntensityUnitsEnum) -> float:
        ...
class FractionUnits:
    class FractionUnitsEnum:
        """
        Members:
        
          Fraction
        
          Percent
        """
        Fraction: typing.ClassVar[FractionUnits.FractionUnitsEnum]  # value = <FractionUnitsEnum.Fraction: 0>
        Percent: typing.ClassVar[FractionUnits.FractionUnitsEnum]  # value = <FractionUnitsEnum.Percent: 1>
        __members__: typing.ClassVar[dict[str, FractionUnits.FractionUnitsEnum]]  # value = {'Fraction': <FractionUnitsEnum.Fraction: 0>, 'Percent': <FractionUnitsEnum.Percent: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Fraction: typing.ClassVar[FractionUnits.FractionUnitsEnum]  # value = <FractionUnitsEnum.Fraction: 0>
    Percent: typing.ClassVar[FractionUnits.FractionUnitsEnum]  # value = <FractionUnitsEnum.Percent: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: FractionUnits.FractionUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: FractionUnits.FractionUnitsEnum) -> float:
        ...
class HeatOfCombustionUnits:
    class HeatOfCombustionUnitsEnum:
        """
        Members:
        
          BtusPerPound
        
          KilojoulesPerKilogram
        """
        BtusPerPound: typing.ClassVar[HeatOfCombustionUnits.HeatOfCombustionUnitsEnum]  # value = <HeatOfCombustionUnitsEnum.BtusPerPound: 0>
        KilojoulesPerKilogram: typing.ClassVar[HeatOfCombustionUnits.HeatOfCombustionUnitsEnum]  # value = <HeatOfCombustionUnitsEnum.KilojoulesPerKilogram: 1>
        __members__: typing.ClassVar[dict[str, HeatOfCombustionUnits.HeatOfCombustionUnitsEnum]]  # value = {'BtusPerPound': <HeatOfCombustionUnitsEnum.BtusPerPound: 0>, 'KilojoulesPerKilogram': <HeatOfCombustionUnitsEnum.KilojoulesPerKilogram: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    BtusPerPound: typing.ClassVar[HeatOfCombustionUnits.HeatOfCombustionUnitsEnum]  # value = <HeatOfCombustionUnitsEnum.BtusPerPound: 0>
    KilojoulesPerKilogram: typing.ClassVar[HeatOfCombustionUnits.HeatOfCombustionUnitsEnum]  # value = <HeatOfCombustionUnitsEnum.KilojoulesPerKilogram: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: HeatOfCombustionUnits.HeatOfCombustionUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: HeatOfCombustionUnits.HeatOfCombustionUnitsEnum) -> float:
        ...
class HeatPerUnitAreaUnits:
    class HeatPerUnitAreaUnitsEnum:
        """
        Members:
        
          BtusPerSquareFoot
        
          KilojoulesPerSquareMeter
        
          KilowattSecondsPerSquareMeter
        """
        BtusPerSquareFoot: typing.ClassVar[HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]  # value = <HeatPerUnitAreaUnitsEnum.BtusPerSquareFoot: 0>
        KilojoulesPerSquareMeter: typing.ClassVar[HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]  # value = <HeatPerUnitAreaUnitsEnum.KilojoulesPerSquareMeter: 1>
        KilowattSecondsPerSquareMeter: typing.ClassVar[HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]  # value = <HeatPerUnitAreaUnitsEnum.KilowattSecondsPerSquareMeter: 2>
        __members__: typing.ClassVar[dict[str, HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]]  # value = {'BtusPerSquareFoot': <HeatPerUnitAreaUnitsEnum.BtusPerSquareFoot: 0>, 'KilojoulesPerSquareMeter': <HeatPerUnitAreaUnitsEnum.KilojoulesPerSquareMeter: 1>, 'KilowattSecondsPerSquareMeter': <HeatPerUnitAreaUnitsEnum.KilowattSecondsPerSquareMeter: 2>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    BtusPerSquareFoot: typing.ClassVar[HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]  # value = <HeatPerUnitAreaUnitsEnum.BtusPerSquareFoot: 0>
    KilojoulesPerSquareMeter: typing.ClassVar[HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]  # value = <HeatPerUnitAreaUnitsEnum.KilojoulesPerSquareMeter: 1>
    KilowattSecondsPerSquareMeter: typing.ClassVar[HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum]  # value = <HeatPerUnitAreaUnitsEnum.KilowattSecondsPerSquareMeter: 2>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: HeatPerUnitAreaUnits.HeatPerUnitAreaUnitsEnum) -> float:
        ...
class HeatSinkUnits:
    class HeatSinkUnitsEnum:
        """
        Members:
        
          BtusPerCubicFoot
        
          KilojoulesPerCubicMeter
        """
        BtusPerCubicFoot: typing.ClassVar[HeatSinkUnits.HeatSinkUnitsEnum]  # value = <HeatSinkUnitsEnum.BtusPerCubicFoot: 0>
        KilojoulesPerCubicMeter: typing.ClassVar[HeatSinkUnits.HeatSinkUnitsEnum]  # value = <HeatSinkUnitsEnum.KilojoulesPerCubicMeter: 1>
        __members__: typing.ClassVar[dict[str, HeatSinkUnits.HeatSinkUnitsEnum]]  # value = {'BtusPerCubicFoot': <HeatSinkUnitsEnum.BtusPerCubicFoot: 0>, 'KilojoulesPerCubicMeter': <HeatSinkUnitsEnum.KilojoulesPerCubicMeter: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    BtusPerCubicFoot: typing.ClassVar[HeatSinkUnits.HeatSinkUnitsEnum]  # value = <HeatSinkUnitsEnum.BtusPerCubicFoot: 0>
    KilojoulesPerCubicMeter: typing.ClassVar[HeatSinkUnits.HeatSinkUnitsEnum]  # value = <HeatSinkUnitsEnum.KilojoulesPerCubicMeter: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: HeatSinkUnits.HeatSinkUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: HeatSinkUnits.HeatSinkUnitsEnum) -> float:
        ...
class HeatSourceAndReactionIntensityUnits:
    class HeatSourceAndReactionIntensityUnitsEnum:
        """
        Members:
        
          BtusPerSquareFootPerMinute
        
          BtusPerSquareFootPerSecond
        
          KilojoulesPerSquareMeterPerSecond
        
          KilojoulesPerSquareMeterPerMinute
        
          KilowattsPerSquareMeter
        """
        BtusPerSquareFootPerMinute: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.BtusPerSquareFootPerMinute: 0>
        BtusPerSquareFootPerSecond: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.BtusPerSquareFootPerSecond: 1>
        KilojoulesPerSquareMeterPerMinute: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.KilojoulesPerSquareMeterPerMinute: 3>
        KilojoulesPerSquareMeterPerSecond: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.KilojoulesPerSquareMeterPerSecond: 2>
        KilowattsPerSquareMeter: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.KilowattsPerSquareMeter: 4>
        __members__: typing.ClassVar[dict[str, HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]]  # value = {'BtusPerSquareFootPerMinute': <HeatSourceAndReactionIntensityUnitsEnum.BtusPerSquareFootPerMinute: 0>, 'BtusPerSquareFootPerSecond': <HeatSourceAndReactionIntensityUnitsEnum.BtusPerSquareFootPerSecond: 1>, 'KilojoulesPerSquareMeterPerSecond': <HeatSourceAndReactionIntensityUnitsEnum.KilojoulesPerSquareMeterPerSecond: 2>, 'KilojoulesPerSquareMeterPerMinute': <HeatSourceAndReactionIntensityUnitsEnum.KilojoulesPerSquareMeterPerMinute: 3>, 'KilowattsPerSquareMeter': <HeatSourceAndReactionIntensityUnitsEnum.KilowattsPerSquareMeter: 4>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    BtusPerSquareFootPerMinute: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.BtusPerSquareFootPerMinute: 0>
    BtusPerSquareFootPerSecond: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.BtusPerSquareFootPerSecond: 1>
    KilojoulesPerSquareMeterPerMinute: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.KilojoulesPerSquareMeterPerMinute: 3>
    KilojoulesPerSquareMeterPerSecond: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.KilojoulesPerSquareMeterPerSecond: 2>
    KilowattsPerSquareMeter: typing.ClassVar[HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum]  # value = <HeatSourceAndReactionIntensityUnitsEnum.KilowattsPerSquareMeter: 4>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: HeatSourceAndReactionIntensityUnits.HeatSourceAndReactionIntensityUnitsEnum) -> float:
        ...
class LengthUnits:
    class LengthUnitsEnum:
        """
        Members:
        
          Feet
        
          Inches
        
          Millimeters
        
          Centimeters
        
          Meters
        
          Chains
        
          Miles
        
          Kilometers
        """
        Centimeters: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Centimeters: 3>
        Chains: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Chains: 5>
        Feet: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Feet: 0>
        Inches: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Inches: 1>
        Kilometers: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Kilometers: 7>
        Meters: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Meters: 4>
        Miles: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Miles: 6>
        Millimeters: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Millimeters: 2>
        __members__: typing.ClassVar[dict[str, LengthUnits.LengthUnitsEnum]]  # value = {'Feet': <LengthUnitsEnum.Feet: 0>, 'Inches': <LengthUnitsEnum.Inches: 1>, 'Millimeters': <LengthUnitsEnum.Millimeters: 2>, 'Centimeters': <LengthUnitsEnum.Centimeters: 3>, 'Meters': <LengthUnitsEnum.Meters: 4>, 'Chains': <LengthUnitsEnum.Chains: 5>, 'Miles': <LengthUnitsEnum.Miles: 6>, 'Kilometers': <LengthUnitsEnum.Kilometers: 7>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Centimeters: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Centimeters: 3>
    Chains: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Chains: 5>
    Feet: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Feet: 0>
    Inches: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Inches: 1>
    Kilometers: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Kilometers: 7>
    Meters: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Meters: 4>
    Miles: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Miles: 6>
    Millimeters: typing.ClassVar[LengthUnits.LengthUnitsEnum]  # value = <LengthUnitsEnum.Millimeters: 2>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: LengthUnits.LengthUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: LengthUnits.LengthUnitsEnum) -> float:
        ...
class LoadingUnits:
    class LoadingUnitsEnum:
        """
        Members:
        
          PoundsPerSquareFoot
        
          TonsPerAcre
        
          TonnesPerHectare
        
          KilogramsPerSquareMeter
        """
        KilogramsPerSquareMeter: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.KilogramsPerSquareMeter: 3>
        PoundsPerSquareFoot: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.PoundsPerSquareFoot: 0>
        TonnesPerHectare: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.TonnesPerHectare: 2>
        TonsPerAcre: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.TonsPerAcre: 1>
        __members__: typing.ClassVar[dict[str, LoadingUnits.LoadingUnitsEnum]]  # value = {'PoundsPerSquareFoot': <LoadingUnitsEnum.PoundsPerSquareFoot: 0>, 'TonsPerAcre': <LoadingUnitsEnum.TonsPerAcre: 1>, 'TonnesPerHectare': <LoadingUnitsEnum.TonnesPerHectare: 2>, 'KilogramsPerSquareMeter': <LoadingUnitsEnum.KilogramsPerSquareMeter: 3>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    KilogramsPerSquareMeter: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.KilogramsPerSquareMeter: 3>
    PoundsPerSquareFoot: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.PoundsPerSquareFoot: 0>
    TonnesPerHectare: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.TonnesPerHectare: 2>
    TonsPerAcre: typing.ClassVar[LoadingUnits.LoadingUnitsEnum]  # value = <LoadingUnitsEnum.TonsPerAcre: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: LoadingUnits.LoadingUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: LoadingUnits.LoadingUnitsEnum) -> float:
        ...
class PressureUnits:
    class PressureUnitsEnum:
        """
        Members:
        
          Pascal
        
          HectoPascal
        
          KiloPascal
        
          MegaPascal
        
          GigaPascal
        
          Bar
        
          Atmosphere
        
          TechnicalAtmosphere
        
          PoundPerSquareInch
        """
        Atmosphere: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.Atmosphere: 6>
        Bar: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.Bar: 5>
        GigaPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.GigaPascal: 4>
        HectoPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.HectoPascal: 1>
        KiloPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.KiloPascal: 2>
        MegaPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.MegaPascal: 3>
        Pascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.Pascal: 0>
        PoundPerSquareInch: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.PoundPerSquareInch: 8>
        TechnicalAtmosphere: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.TechnicalAtmosphere: 7>
        __members__: typing.ClassVar[dict[str, PressureUnits.PressureUnitsEnum]]  # value = {'Pascal': <PressureUnitsEnum.Pascal: 0>, 'HectoPascal': <PressureUnitsEnum.HectoPascal: 1>, 'KiloPascal': <PressureUnitsEnum.KiloPascal: 2>, 'MegaPascal': <PressureUnitsEnum.MegaPascal: 3>, 'GigaPascal': <PressureUnitsEnum.GigaPascal: 4>, 'Bar': <PressureUnitsEnum.Bar: 5>, 'Atmosphere': <PressureUnitsEnum.Atmosphere: 6>, 'TechnicalAtmosphere': <PressureUnitsEnum.TechnicalAtmosphere: 7>, 'PoundPerSquareInch': <PressureUnitsEnum.PoundPerSquareInch: 8>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Atmosphere: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.Atmosphere: 6>
    Bar: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.Bar: 5>
    GigaPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.GigaPascal: 4>
    HectoPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.HectoPascal: 1>
    KiloPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.KiloPascal: 2>
    MegaPascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.MegaPascal: 3>
    Pascal: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.Pascal: 0>
    PoundPerSquareInch: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.PoundPerSquareInch: 8>
    TechnicalAtmosphere: typing.ClassVar[PressureUnits.PressureUnitsEnum]  # value = <PressureUnitsEnum.TechnicalAtmosphere: 7>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: PressureUnits.PressureUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: PressureUnits.PressureUnitsEnum) -> float:
        ...
class SlopeUnits:
    class SlopeUnitsEnum:
        """
        Members:
        
          Degrees
        
          Percent
        """
        Degrees: typing.ClassVar[SlopeUnits.SlopeUnitsEnum]  # value = <SlopeUnitsEnum.Degrees: 0>
        Percent: typing.ClassVar[SlopeUnits.SlopeUnitsEnum]  # value = <SlopeUnitsEnum.Percent: 1>
        __members__: typing.ClassVar[dict[str, SlopeUnits.SlopeUnitsEnum]]  # value = {'Degrees': <SlopeUnitsEnum.Degrees: 0>, 'Percent': <SlopeUnitsEnum.Percent: 1>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Degrees: typing.ClassVar[SlopeUnits.SlopeUnitsEnum]  # value = <SlopeUnitsEnum.Degrees: 0>
    Percent: typing.ClassVar[SlopeUnits.SlopeUnitsEnum]  # value = <SlopeUnitsEnum.Percent: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: SlopeUnits.SlopeUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: SlopeUnits.SlopeUnitsEnum) -> float:
        ...
class SpeedUnits:
    class SpeedUnitsEnum:
        """
        Members:
        
          FeetPerMinute
        
          ChainsPerHour
        
          MetersPerSecond
        
          MetersPerMinute
        
          MetersPerHour
        
          MilesPerHour
        
          KilometersPerHour
        """
        ChainsPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.ChainsPerHour: 1>
        FeetPerMinute: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.FeetPerMinute: 0>
        KilometersPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.KilometersPerHour: 6>
        MetersPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MetersPerHour: 4>
        MetersPerMinute: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MetersPerMinute: 3>
        MetersPerSecond: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MetersPerSecond: 2>
        MilesPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MilesPerHour: 5>
        __members__: typing.ClassVar[dict[str, SpeedUnits.SpeedUnitsEnum]]  # value = {'FeetPerMinute': <SpeedUnitsEnum.FeetPerMinute: 0>, 'ChainsPerHour': <SpeedUnitsEnum.ChainsPerHour: 1>, 'MetersPerSecond': <SpeedUnitsEnum.MetersPerSecond: 2>, 'MetersPerMinute': <SpeedUnitsEnum.MetersPerMinute: 3>, 'MetersPerHour': <SpeedUnitsEnum.MetersPerHour: 4>, 'MilesPerHour': <SpeedUnitsEnum.MilesPerHour: 5>, 'KilometersPerHour': <SpeedUnitsEnum.KilometersPerHour: 6>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    ChainsPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.ChainsPerHour: 1>
    FeetPerMinute: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.FeetPerMinute: 0>
    KilometersPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.KilometersPerHour: 6>
    MetersPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MetersPerHour: 4>
    MetersPerMinute: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MetersPerMinute: 3>
    MetersPerSecond: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MetersPerSecond: 2>
    MilesPerHour: typing.ClassVar[SpeedUnits.SpeedUnitsEnum]  # value = <SpeedUnitsEnum.MilesPerHour: 5>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: SpeedUnits.SpeedUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: SpeedUnits.SpeedUnitsEnum) -> float:
        ...
class SurfaceAreaToVolumeUnits:
    class SurfaceAreaToVolumeUnitsEnum:
        """
        Members:
        
          SquareFeetOverCubicFeet
        
          SquareMetersOverCubicMeters
        
          SquareInchesOverCubicInches
        
          SquareCentimetersOverCubicCentimeters
        """
        SquareCentimetersOverCubicCentimeters: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareCentimetersOverCubicCentimeters: 3>
        SquareFeetOverCubicFeet: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareFeetOverCubicFeet: 0>
        SquareInchesOverCubicInches: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareInchesOverCubicInches: 2>
        SquareMetersOverCubicMeters: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareMetersOverCubicMeters: 1>
        __members__: typing.ClassVar[dict[str, SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]]  # value = {'SquareFeetOverCubicFeet': <SurfaceAreaToVolumeUnitsEnum.SquareFeetOverCubicFeet: 0>, 'SquareMetersOverCubicMeters': <SurfaceAreaToVolumeUnitsEnum.SquareMetersOverCubicMeters: 1>, 'SquareInchesOverCubicInches': <SurfaceAreaToVolumeUnitsEnum.SquareInchesOverCubicInches: 2>, 'SquareCentimetersOverCubicCentimeters': <SurfaceAreaToVolumeUnitsEnum.SquareCentimetersOverCubicCentimeters: 3>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    SquareCentimetersOverCubicCentimeters: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareCentimetersOverCubicCentimeters: 3>
    SquareFeetOverCubicFeet: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareFeetOverCubicFeet: 0>
    SquareInchesOverCubicInches: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareInchesOverCubicInches: 2>
    SquareMetersOverCubicMeters: typing.ClassVar[SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum]  # value = <SurfaceAreaToVolumeUnitsEnum.SquareMetersOverCubicMeters: 1>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: SurfaceAreaToVolumeUnits.SurfaceAreaToVolumeUnitsEnum) -> float:
        ...
class TemperatureUnits:
    class TemperatureUnitsEnum:
        """
        Members:
        
          Fahrenheit
        
          Celsius
        
          Kelvin
        """
        Celsius: typing.ClassVar[TemperatureUnits.TemperatureUnitsEnum]  # value = <TemperatureUnitsEnum.Celsius: 1>
        Fahrenheit: typing.ClassVar[TemperatureUnits.TemperatureUnitsEnum]  # value = <TemperatureUnitsEnum.Fahrenheit: 0>
        Kelvin: typing.ClassVar[TemperatureUnits.TemperatureUnitsEnum]  # value = <TemperatureUnitsEnum.Kelvin: 2>
        __members__: typing.ClassVar[dict[str, TemperatureUnits.TemperatureUnitsEnum]]  # value = {'Fahrenheit': <TemperatureUnitsEnum.Fahrenheit: 0>, 'Celsius': <TemperatureUnitsEnum.Celsius: 1>, 'Kelvin': <TemperatureUnitsEnum.Kelvin: 2>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Celsius: typing.ClassVar[TemperatureUnits.TemperatureUnitsEnum]  # value = <TemperatureUnitsEnum.Celsius: 1>
    Fahrenheit: typing.ClassVar[TemperatureUnits.TemperatureUnitsEnum]  # value = <TemperatureUnitsEnum.Fahrenheit: 0>
    Kelvin: typing.ClassVar[TemperatureUnits.TemperatureUnitsEnum]  # value = <TemperatureUnitsEnum.Kelvin: 2>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: TemperatureUnits.TemperatureUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: TemperatureUnits.TemperatureUnitsEnum) -> float:
        ...
class TimeUnits:
    class TimeUnitsEnum:
        """
        Members:
        
          Minutes
        
          Seconds
        
          Hours
        
          Days
        
          Years
        """
        Days: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Days: 3>
        Hours: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Hours: 2>
        Minutes: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Minutes: 0>
        Seconds: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Seconds: 1>
        Years: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Years: 4>
        __members__: typing.ClassVar[dict[str, TimeUnits.TimeUnitsEnum]]  # value = {'Minutes': <TimeUnitsEnum.Minutes: 0>, 'Seconds': <TimeUnitsEnum.Seconds: 1>, 'Hours': <TimeUnitsEnum.Hours: 2>, 'Days': <TimeUnitsEnum.Days: 3>, 'Years': <TimeUnitsEnum.Years: 4>}
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Days: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Days: 3>
    Hours: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Hours: 2>
    Minutes: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Minutes: 0>
    Seconds: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Seconds: 1>
    Years: typing.ClassVar[TimeUnits.TimeUnitsEnum]  # value = <TimeUnitsEnum.Years: 4>
    @staticmethod
    def fromBaseUnits(arg0: float, arg1: TimeUnits.TimeUnitsEnum) -> float:
        ...
    @staticmethod
    def toBaseUnits(arg0: float, arg1: TimeUnits.TimeUnitsEnum) -> float:
        ...
