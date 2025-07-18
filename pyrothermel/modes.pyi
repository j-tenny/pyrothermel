"""
Calculation modes
"""
from __future__ import annotations
import typing
__all__ = ['AllAggregate', 'Arithmetic', 'AspenFireSeverity', 'BySizeClass', 'Chamise', 'ChaparralContants', 'ChaparralFuelInputLoadMode', 'ChaparralFuelType', 'Dead', 'DeadAggregate', 'DeadAggregateAndLiveSizeClass', 'DirectFuelLoad', 'DirectMidflame', 'DontUseCrownRatio', 'First', 'FromIgnitionPoint', 'FromPerimeter', 'FuelConstants', 'FuelLifeState', 'FuelLoadFromDepthAndChaparralType', 'Harmonic', 'HundredHour', 'Live', 'LiveAggregate', 'LiveAggregateAndDeadSizeClass', 'LiveHerbaceous', 'LiveWoody', 'Low', 'MaxDeadSizeClasses', 'MaxFuelModels', 'MaxLifeStates', 'MaxLiveSizeClasses', 'MaxParticles', 'MaxSavrSizeClasses', 'MixedBrush', 'Moderate', 'MoistureClassInput', 'MoistureInputMode', 'MoistureScenario', 'NoMethod', 'NotSet', 'NumFuelClasses', 'NumberOfModels', 'OneHour', 'RelativeToNorth', 'RelativeToUpslope', 'Second', 'Sheltered', 'SurfaceFireSpreadDirectionMode', 'TenHour', 'TenMeter', 'TwentyFoot', 'TwoDimensional', 'TwoFuelModelsContants', 'TwoFuelModelsMethod', 'Unsheltered', 'UseCrownRatio', 'UserInput', 'WindAdjustmentFactorCalculationMethod', 'WindAdjustmentFactorShelterMethod', 'WindAndSpreadOrientationMode', 'WindHeightInputMode']
class AspenFireSeverity:
    """
    Members:
    
      Low
    
      Moderate
    """
    Low: typing.ClassVar[AspenFireSeverity]  # value = <AspenFireSeverity.Low: 0>
    Moderate: typing.ClassVar[AspenFireSeverity]  # value = <AspenFireSeverity.Moderate: 1>
    __members__: typing.ClassVar[dict[str, AspenFireSeverity]]  # value = {'Low': <AspenFireSeverity.Low: 0>, 'Moderate': <AspenFireSeverity.Moderate: 1>}
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
class ChaparralContants:
    """
    Members:
    
      NumFuelClasses
    """
    NumFuelClasses: typing.ClassVar[ChaparralContants]  # value = <ChaparralContants.NumFuelClasses: 5>
    __members__: typing.ClassVar[dict[str, ChaparralContants]]  # value = {'NumFuelClasses': <ChaparralContants.NumFuelClasses: 5>}
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
class ChaparralFuelInputLoadMode:
    """
    Members:
    
      DirectFuelLoad
    
      FuelLoadFromDepthAndChaparralType
    """
    DirectFuelLoad: typing.ClassVar[ChaparralFuelInputLoadMode]  # value = <ChaparralFuelInputLoadMode.DirectFuelLoad: 1>
    FuelLoadFromDepthAndChaparralType: typing.ClassVar[ChaparralFuelInputLoadMode]  # value = <ChaparralFuelInputLoadMode.FuelLoadFromDepthAndChaparralType: 2>
    __members__: typing.ClassVar[dict[str, ChaparralFuelInputLoadMode]]  # value = {'DirectFuelLoad': <ChaparralFuelInputLoadMode.DirectFuelLoad: 1>, 'FuelLoadFromDepthAndChaparralType': <ChaparralFuelInputLoadMode.FuelLoadFromDepthAndChaparralType: 2>}
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
class ChaparralFuelType:
    """
    Members:
    
      NotSet
    
      Chamise
    
      MixedBrush
    """
    Chamise: typing.ClassVar[ChaparralFuelType]  # value = <ChaparralFuelType.Chamise: 1>
    MixedBrush: typing.ClassVar[ChaparralFuelType]  # value = <ChaparralFuelType.MixedBrush: 2>
    NotSet: typing.ClassVar[ChaparralFuelType]  # value = <ChaparralFuelType.NotSet: 0>
    __members__: typing.ClassVar[dict[str, ChaparralFuelType]]  # value = {'NotSet': <ChaparralFuelType.NotSet: 0>, 'Chamise': <ChaparralFuelType.Chamise: 1>, 'MixedBrush': <ChaparralFuelType.MixedBrush: 2>}
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
class FuelConstants:
    """
    Members:
    
      MaxLifeStates
    
      MaxLiveSizeClasses
    
      MaxDeadSizeClasses
    
      MaxParticles
    
      MaxSavrSizeClasses
    
      MaxFuelModels
    """
    MaxDeadSizeClasses: typing.ClassVar[FuelConstants]  # value = <FuelConstants.MaxDeadSizeClasses: 4>
    MaxFuelModels: typing.ClassVar[FuelConstants]  # value = <FuelConstants.MaxFuelModels: 256>
    MaxLifeStates: typing.ClassVar[FuelConstants]  # value = <FuelConstants.MaxLifeStates: 2>
    MaxLiveSizeClasses: typing.ClassVar[FuelConstants]  # value = <FuelConstants.MaxLiveSizeClasses: 5>
    MaxParticles: typing.ClassVar[FuelConstants]  # value = <FuelConstants.MaxLiveSizeClasses: 5>
    MaxSavrSizeClasses: typing.ClassVar[FuelConstants]  # value = <FuelConstants.MaxLiveSizeClasses: 5>
    __members__: typing.ClassVar[dict[str, FuelConstants]]  # value = {'MaxLifeStates': <FuelConstants.MaxLifeStates: 2>, 'MaxLiveSizeClasses': <FuelConstants.MaxLiveSizeClasses: 5>, 'MaxDeadSizeClasses': <FuelConstants.MaxDeadSizeClasses: 4>, 'MaxParticles': <FuelConstants.MaxLiveSizeClasses: 5>, 'MaxSavrSizeClasses': <FuelConstants.MaxLiveSizeClasses: 5>, 'MaxFuelModels': <FuelConstants.MaxFuelModels: 256>}
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
class FuelLifeState:
    """
    Members:
    
      Dead
    
      Live
    """
    Dead: typing.ClassVar[FuelLifeState]  # value = <FuelLifeState.Dead: 0>
    Live: typing.ClassVar[FuelLifeState]  # value = <FuelLifeState.Live: 1>
    __members__: typing.ClassVar[dict[str, FuelLifeState]]  # value = {'Dead': <FuelLifeState.Dead: 0>, 'Live': <FuelLifeState.Live: 1>}
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
class MoistureClassInput:
    """
    Members:
    
      OneHour
    
      TenHour
    
      HundredHour
    
      LiveHerbaceous
    
      LiveWoody
    
      DeadAggregate
    
      LiveAggregate
    """
    DeadAggregate: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.DeadAggregate: 5>
    HundredHour: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.HundredHour: 2>
    LiveAggregate: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.LiveAggregate: 6>
    LiveHerbaceous: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.LiveHerbaceous: 3>
    LiveWoody: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.LiveWoody: 4>
    OneHour: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.OneHour: 0>
    TenHour: typing.ClassVar[MoistureClassInput]  # value = <MoistureClassInput.TenHour: 1>
    __members__: typing.ClassVar[dict[str, MoistureClassInput]]  # value = {'OneHour': <MoistureClassInput.OneHour: 0>, 'TenHour': <MoistureClassInput.TenHour: 1>, 'HundredHour': <MoistureClassInput.HundredHour: 2>, 'LiveHerbaceous': <MoistureClassInput.LiveHerbaceous: 3>, 'LiveWoody': <MoistureClassInput.LiveWoody: 4>, 'DeadAggregate': <MoistureClassInput.DeadAggregate: 5>, 'LiveAggregate': <MoistureClassInput.LiveAggregate: 6>}
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
class MoistureInputMode:
    """
    Members:
    
      BySizeClass
    
      AllAggregate
    
      DeadAggregateAndLiveSizeClass
    
      LiveAggregateAndDeadSizeClass
    
      MoistureScenario
    """
    AllAggregate: typing.ClassVar[MoistureInputMode]  # value = <MoistureInputMode.AllAggregate: 1>
    BySizeClass: typing.ClassVar[MoistureInputMode]  # value = <MoistureInputMode.BySizeClass: 0>
    DeadAggregateAndLiveSizeClass: typing.ClassVar[MoistureInputMode]  # value = <MoistureInputMode.DeadAggregateAndLiveSizeClass: 2>
    LiveAggregateAndDeadSizeClass: typing.ClassVar[MoistureInputMode]  # value = <MoistureInputMode.LiveAggregateAndDeadSizeClass: 3>
    MoistureScenario: typing.ClassVar[MoistureInputMode]  # value = <MoistureInputMode.MoistureScenario: 4>
    __members__: typing.ClassVar[dict[str, MoistureInputMode]]  # value = {'BySizeClass': <MoistureInputMode.BySizeClass: 0>, 'AllAggregate': <MoistureInputMode.AllAggregate: 1>, 'DeadAggregateAndLiveSizeClass': <MoistureInputMode.DeadAggregateAndLiveSizeClass: 2>, 'LiveAggregateAndDeadSizeClass': <MoistureInputMode.LiveAggregateAndDeadSizeClass: 3>, 'MoistureScenario': <MoistureInputMode.MoistureScenario: 4>}
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
class SurfaceFireSpreadDirectionMode:
    """
    Members:
    
      FromIgnitionPoint
    
      FromPerimeter
    """
    FromIgnitionPoint: typing.ClassVar[SurfaceFireSpreadDirectionMode]  # value = <SurfaceFireSpreadDirectionMode.FromIgnitionPoint: 0>
    FromPerimeter: typing.ClassVar[SurfaceFireSpreadDirectionMode]  # value = <SurfaceFireSpreadDirectionMode.FromPerimeter: 1>
    __members__: typing.ClassVar[dict[str, SurfaceFireSpreadDirectionMode]]  # value = {'FromIgnitionPoint': <SurfaceFireSpreadDirectionMode.FromIgnitionPoint: 0>, 'FromPerimeter': <SurfaceFireSpreadDirectionMode.FromPerimeter: 1>}
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
class TwoFuelModelsContants:
    """
    Members:
    
      First
    
      Second
    
      NumberOfModels
    """
    First: typing.ClassVar[TwoFuelModelsContants]  # value = <TwoFuelModelsContants.First: 0>
    NumberOfModels: typing.ClassVar[TwoFuelModelsContants]  # value = <TwoFuelModelsContants.NumberOfModels: 2>
    Second: typing.ClassVar[TwoFuelModelsContants]  # value = <TwoFuelModelsContants.Second: 1>
    __members__: typing.ClassVar[dict[str, TwoFuelModelsContants]]  # value = {'First': <TwoFuelModelsContants.First: 0>, 'Second': <TwoFuelModelsContants.Second: 1>, 'NumberOfModels': <TwoFuelModelsContants.NumberOfModels: 2>}
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
class TwoFuelModelsMethod:
    """
    Members:
    
      NoMethod
    
      Arithmetic
    
      Harmonic
    
      TwoDimensional
    """
    Arithmetic: typing.ClassVar[TwoFuelModelsMethod]  # value = <TwoFuelModelsMethod.Arithmetic: 1>
    Harmonic: typing.ClassVar[TwoFuelModelsMethod]  # value = <TwoFuelModelsMethod.Harmonic: 2>
    NoMethod: typing.ClassVar[TwoFuelModelsMethod]  # value = <TwoFuelModelsMethod.NoMethod: 0>
    TwoDimensional: typing.ClassVar[TwoFuelModelsMethod]  # value = <TwoFuelModelsMethod.TwoDimensional: 3>
    __members__: typing.ClassVar[dict[str, TwoFuelModelsMethod]]  # value = {'NoMethod': <TwoFuelModelsMethod.NoMethod: 0>, 'Arithmetic': <TwoFuelModelsMethod.Arithmetic: 1>, 'Harmonic': <TwoFuelModelsMethod.Harmonic: 2>, 'TwoDimensional': <TwoFuelModelsMethod.TwoDimensional: 3>}
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
class WindAdjustmentFactorCalculationMethod:
    """
    Members:
    
      UserInput
    
      UseCrownRatio
    
      DontUseCrownRatio
    """
    DontUseCrownRatio: typing.ClassVar[WindAdjustmentFactorCalculationMethod]  # value = <WindAdjustmentFactorCalculationMethod.DontUseCrownRatio: 2>
    UseCrownRatio: typing.ClassVar[WindAdjustmentFactorCalculationMethod]  # value = <WindAdjustmentFactorCalculationMethod.UseCrownRatio: 1>
    UserInput: typing.ClassVar[WindAdjustmentFactorCalculationMethod]  # value = <WindAdjustmentFactorCalculationMethod.UserInput: 0>
    __members__: typing.ClassVar[dict[str, WindAdjustmentFactorCalculationMethod]]  # value = {'UserInput': <WindAdjustmentFactorCalculationMethod.UserInput: 0>, 'UseCrownRatio': <WindAdjustmentFactorCalculationMethod.UseCrownRatio: 1>, 'DontUseCrownRatio': <WindAdjustmentFactorCalculationMethod.DontUseCrownRatio: 2>}
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
class WindAdjustmentFactorShelterMethod:
    """
    Members:
    
      Unsheltered
    
      Sheltered
    """
    Sheltered: typing.ClassVar[WindAdjustmentFactorShelterMethod]  # value = <WindAdjustmentFactorShelterMethod.Sheltered: 1>
    Unsheltered: typing.ClassVar[WindAdjustmentFactorShelterMethod]  # value = <WindAdjustmentFactorShelterMethod.Unsheltered: 0>
    __members__: typing.ClassVar[dict[str, WindAdjustmentFactorShelterMethod]]  # value = {'Unsheltered': <WindAdjustmentFactorShelterMethod.Unsheltered: 0>, 'Sheltered': <WindAdjustmentFactorShelterMethod.Sheltered: 1>}
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
class WindAndSpreadOrientationMode:
    """
    Members:
    
      RelativeToUpslope
    
      RelativeToNorth
    """
    RelativeToNorth: typing.ClassVar[WindAndSpreadOrientationMode]  # value = <WindAndSpreadOrientationMode.RelativeToNorth: 1>
    RelativeToUpslope: typing.ClassVar[WindAndSpreadOrientationMode]  # value = <WindAndSpreadOrientationMode.RelativeToUpslope: 0>
    __members__: typing.ClassVar[dict[str, WindAndSpreadOrientationMode]]  # value = {'RelativeToUpslope': <WindAndSpreadOrientationMode.RelativeToUpslope: 0>, 'RelativeToNorth': <WindAndSpreadOrientationMode.RelativeToNorth: 1>}
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
class WindHeightInputMode:
    """
    Members:
    
      DirectMidflame
    
      TwentyFoot
    
      TenMeter
    """
    DirectMidflame: typing.ClassVar[WindHeightInputMode]  # value = <WindHeightInputMode.DirectMidflame: 0>
    TenMeter: typing.ClassVar[WindHeightInputMode]  # value = <WindHeightInputMode.TenMeter: 2>
    TwentyFoot: typing.ClassVar[WindHeightInputMode]  # value = <WindHeightInputMode.TwentyFoot: 1>
    __members__: typing.ClassVar[dict[str, WindHeightInputMode]]  # value = {'DirectMidflame': <WindHeightInputMode.DirectMidflame: 0>, 'TwentyFoot': <WindHeightInputMode.TwentyFoot: 1>, 'TenMeter': <WindHeightInputMode.TenMeter: 2>}
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
AllAggregate: MoistureInputMode  # value = <MoistureInputMode.AllAggregate: 1>
Arithmetic: TwoFuelModelsMethod  # value = <TwoFuelModelsMethod.Arithmetic: 1>
BySizeClass: MoistureInputMode  # value = <MoistureInputMode.BySizeClass: 0>
Chamise: ChaparralFuelType  # value = <ChaparralFuelType.Chamise: 1>
Dead: FuelLifeState  # value = <FuelLifeState.Dead: 0>
DeadAggregate: MoistureClassInput  # value = <MoistureClassInput.DeadAggregate: 5>
DeadAggregateAndLiveSizeClass: MoistureInputMode  # value = <MoistureInputMode.DeadAggregateAndLiveSizeClass: 2>
DirectFuelLoad: ChaparralFuelInputLoadMode  # value = <ChaparralFuelInputLoadMode.DirectFuelLoad: 1>
DirectMidflame: WindHeightInputMode  # value = <WindHeightInputMode.DirectMidflame: 0>
DontUseCrownRatio: WindAdjustmentFactorCalculationMethod  # value = <WindAdjustmentFactorCalculationMethod.DontUseCrownRatio: 2>
First: TwoFuelModelsContants  # value = <TwoFuelModelsContants.First: 0>
FromIgnitionPoint: SurfaceFireSpreadDirectionMode  # value = <SurfaceFireSpreadDirectionMode.FromIgnitionPoint: 0>
FromPerimeter: SurfaceFireSpreadDirectionMode  # value = <SurfaceFireSpreadDirectionMode.FromPerimeter: 1>
FuelLoadFromDepthAndChaparralType: ChaparralFuelInputLoadMode  # value = <ChaparralFuelInputLoadMode.FuelLoadFromDepthAndChaparralType: 2>
Harmonic: TwoFuelModelsMethod  # value = <TwoFuelModelsMethod.Harmonic: 2>
HundredHour: MoistureClassInput  # value = <MoistureClassInput.HundredHour: 2>
Live: FuelLifeState  # value = <FuelLifeState.Live: 1>
LiveAggregate: MoistureClassInput  # value = <MoistureClassInput.LiveAggregate: 6>
LiveAggregateAndDeadSizeClass: MoistureInputMode  # value = <MoistureInputMode.LiveAggregateAndDeadSizeClass: 3>
LiveHerbaceous: MoistureClassInput  # value = <MoistureClassInput.LiveHerbaceous: 3>
LiveWoody: MoistureClassInput  # value = <MoistureClassInput.LiveWoody: 4>
Low: AspenFireSeverity  # value = <AspenFireSeverity.Low: 0>
MaxDeadSizeClasses: FuelConstants  # value = <FuelConstants.MaxDeadSizeClasses: 4>
MaxFuelModels: FuelConstants  # value = <FuelConstants.MaxFuelModels: 256>
MaxLifeStates: FuelConstants  # value = <FuelConstants.MaxLifeStates: 2>
MaxLiveSizeClasses: FuelConstants  # value = <FuelConstants.MaxLiveSizeClasses: 5>
MaxParticles: FuelConstants  # value = <FuelConstants.MaxLiveSizeClasses: 5>
MaxSavrSizeClasses: FuelConstants  # value = <FuelConstants.MaxLiveSizeClasses: 5>
MixedBrush: ChaparralFuelType  # value = <ChaparralFuelType.MixedBrush: 2>
Moderate: AspenFireSeverity  # value = <AspenFireSeverity.Moderate: 1>
MoistureScenario: MoistureInputMode  # value = <MoistureInputMode.MoistureScenario: 4>
NoMethod: TwoFuelModelsMethod  # value = <TwoFuelModelsMethod.NoMethod: 0>
NotSet: ChaparralFuelType  # value = <ChaparralFuelType.NotSet: 0>
NumFuelClasses: ChaparralContants  # value = <ChaparralContants.NumFuelClasses: 5>
NumberOfModels: TwoFuelModelsContants  # value = <TwoFuelModelsContants.NumberOfModels: 2>
OneHour: MoistureClassInput  # value = <MoistureClassInput.OneHour: 0>
RelativeToNorth: WindAndSpreadOrientationMode  # value = <WindAndSpreadOrientationMode.RelativeToNorth: 1>
RelativeToUpslope: WindAndSpreadOrientationMode  # value = <WindAndSpreadOrientationMode.RelativeToUpslope: 0>
Second: TwoFuelModelsContants  # value = <TwoFuelModelsContants.Second: 1>
Sheltered: WindAdjustmentFactorShelterMethod  # value = <WindAdjustmentFactorShelterMethod.Sheltered: 1>
TenHour: MoistureClassInput  # value = <MoistureClassInput.TenHour: 1>
TenMeter: WindHeightInputMode  # value = <WindHeightInputMode.TenMeter: 2>
TwentyFoot: WindHeightInputMode  # value = <WindHeightInputMode.TwentyFoot: 1>
TwoDimensional: TwoFuelModelsMethod  # value = <TwoFuelModelsMethod.TwoDimensional: 3>
Unsheltered: WindAdjustmentFactorShelterMethod  # value = <WindAdjustmentFactorShelterMethod.Unsheltered: 0>
UseCrownRatio: WindAdjustmentFactorCalculationMethod  # value = <WindAdjustmentFactorCalculationMethod.UseCrownRatio: 1>
UserInput: WindAdjustmentFactorCalculationMethod  # value = <WindAdjustmentFactorCalculationMethod.UserInput: 0>
