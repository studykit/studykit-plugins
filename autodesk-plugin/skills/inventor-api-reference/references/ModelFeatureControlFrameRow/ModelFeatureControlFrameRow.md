# ModelFeatureControlFrameRow Object

## Description

Object represents a row within a feature control frame symbol.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_Delete.md) | Method that deletes the row of the feature control frame, If this is not the last row of the feature control frame, all the rows below this row are also deleted. The first row of the symbol cannot be deleted, so this method will return an error. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [DisplayCommonZoneModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_DisplayCommonZoneModifier.md) | Gets and sets whether to display the common zone modifier or not. |
| [DisplayFreeStateModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_DisplayFreeStateModifier.md) | Gets and sets whether to display the free state modifier or not. |
| [DisplayProjectedToleranceZoneModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_DisplayProjectedToleranceZoneModifier.md) | Gets and sets whether to display the projected tolerance zone modifier or not. |
| [DisplayStatisticalModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_DisplayStatisticalModifier.md) | Gets and sets whether to display the statistical modifier or not. |
| [DisplayTangentPlaneModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_DisplayTangentPlaneModifier.md) | Gets and sets whether to display the tangent plane modifier or not. |
| [DisplayUnequallyDisposedModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_DisplayUnequallyDisposedModifier.md) | Gets and sets whether to display the unequally disposed modifier or not. |
| [GeneralProfileOfSurfaceModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_GeneralProfileOfSurfaceModifier.md) | Gets and sets the flag whether this FCF represents general surface profile tolerance. |
| [GeometricCharacteristic](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_GeometricCharacteristic.md) | Gets and sets the geometric characteristic symbol for the row. |
| [InternalName](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_InternalName.md) | Gets the internal name (GUID) of the model feature control frame row. |
| [Parent](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PrimaryCompoundDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_PrimaryCompoundDatumIdentifier.md) | Gets and sets the primary comopund datum. |
| [PrimaryCompoundDatumModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_PrimaryCompoundDatumModifier.md) | Gets and sets the primary compound datum modifier. |
| [PrimaryDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_PrimaryDatumIdentifier.md) | Gets and sets the primary datum. |
| [PrimaryDatumModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_PrimaryDatumModifier.md) | Gets and sets the the material condition symbol to append to the primary datum. |
| [ProjectedToleranceZonePrecision](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_ProjectedToleranceZonePrecision.md) | Gets and sets the Projected Tolerance Zone precision associated with this geometric characteristic. The value is a short integer. |
| [ProjectedToleranceZoneValue](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_ProjectedToleranceZoneValue.md) | Gets and sets the value for the projected tolerance zone modifier. |
| [SecondaryCompoundDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_SecondaryCompoundDatumIdentifier.md) | Gets and sets the secondary compound datum. |
| [SecondaryCompoundDatumModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_SecondaryCompoundDatumModifier.md) | Gets and sets the secondary compound datum modifier. |
| [SecondaryDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_SecondaryDatumIdentifier.md) | Gets and sets the secondary datum. |
| [SecondaryDatumModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_SecondaryDatumModifier.md) | Gets and sets the material condition symbol to append to the secondary datum. |
| [TertiaryCompoundDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TertiaryCompoundDatumIdentifier.md) | Gets and sets the tertiary compound datum. |
| [TertiaryCompoundDatumModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TertiaryCompoundDatumModifier.md) | Gets and sets the tertiary compound datum modifier. |
| [TertiaryDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TertiaryDatumIdentifier.md) | Gets and sets the tertiary datum. |
| [TertiaryDatumModifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TertiaryDatumModifier.md) | Gets and sets the material condition symbol to append to the tertiary datum. |
| [Tolerance](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_Tolerance.md) | Gets and sets the tolerance associated with this geometric characteristic. The value can be either in centimeters or radians depending on if the geometric characteristic defines a length or angle. |
| [ToleranceMaterialCondition](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_ToleranceMaterialCondition.md) | Gets and sets the symbol to use as tolerance material condition. Valid values are kGDTNoSymbol, kGDTMaximumMaterialCondition and kGDTLeastMaterialCondition. |
| [ToleranceModifierPrefix](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_ToleranceModifierPrefix.md) | Gets and sets the symbol to use as a prefix for the tolerance. |
| [TolerancePrecision](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TolerancePrecision.md) | Gets and sets the tolerance precision associated with this geometric characteristic. The value is a short integer. |
| [Type](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_Type.md) | Gets the constant that indicates the type of this object. |
| [UnequallyDisposedPrecision](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_UnequallyDisposedPrecision.md) | Gets and sets the Unequally Disposed precision associated with this geometric characteristic. The value is a short integer. |
| [UnequallyDisposedValue](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_UnequallyDisposedValue.md) | Gets and sets the value for the unequally disposed modifier. |

## Accessed From

[ModelFeatureControlFrameRows.Add](../ModelFeatureControlFrameRows/ModelFeatureControlFrameRows_Add.md), [ModelFeatureControlFrameRows.Item](../ModelFeatureControlFrameRows/ModelFeatureControlFrameRows_Item.md)

## Version

Introduced in version 2018
