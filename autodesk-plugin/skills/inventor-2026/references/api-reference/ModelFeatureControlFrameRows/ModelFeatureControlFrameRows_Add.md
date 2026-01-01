# ModelFeatureControlFrameRows.Add Method

Parent Object: [ModelFeatureControlFrameRows](../ModelFeatureControlFrameRows/ModelFeatureControlFrameRows.md)

## Description

Method that adds a row to the feature control frame.

## Syntax

ModelFeatureControlFrameRows.**Add**( ***GeometricCharacteristic*** As [GeometricCharacteristicEnum](../GeometricCharacteristicEnum.md), ***Tolerance*** As Double, [***ToleranceModifierPrefix***] As [GDTSymbolEnum](../GDTSymbolEnum.md), [***ToleranceMaterialCondition***] As [GDTSymbolEnum](../GDTSymbolEnum.md), [***PrimaryDatumIdentifier***] As Variant, [***PrimaryDatumModifier***] As [GDTSymbolEnum](../GDTSymbolEnum.md), [***SecondaryDatumIdentifier***] As Variant, [***SecondaryDatumModifier***] As [GDTSymbolEnum](../GDTSymbolEnum.md), [***TertiaryDatumIdentifier***] As Variant, [***TertiaryDatumModifier***] As [GDTSymbolEnum](../GDTSymbolEnum.md) ) As [ModelFeatureControlFrameRow](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometricCharacteristic | [GeometricCharacteristicEnum](../GeometricCharacteristicEnum.md) | Input GeometricCharacteristicEnum that specifies the geometric characteristic symbol for the row. |
| Tolerance | Double | Input Double that specifies the tolerance associated with this geometric characteristic. For length values the units for the value is always centimeters and for angles the value is always radians. The actual displayed value will use the units and precision specified by the style. |
| ToleranceModifierPrefix | [GDTSymbolEnum](../GDTSymbolEnum.md) | Optional input GDTSymbolEnum that specifies a symbol to use as a prefix for the tolerance. For example, the **n** symbol is used when the tolerance zone is cylindrical. |
| ToleranceMaterialCondition | [GDTSymbolEnum](../GDTSymbolEnum.md) | Optional input GDTSymbolEnum that specifies a symbol to use as material condition for the tolerance. For example, the **m** symbol is used to specify maximum material condition. Valid values for this argument are kGDTNoSymbol, kGDTMaximumMaterialCondition and kGDTLeastMaterialCondition.   This is an optional argument whose default value is 104193. |
| PrimaryDatumIdentifier | Variant | Optional input ModelDatumIdentifier object that specifies the primary datum reference. If the geometric characteristic is kStraightness, kFlatness, kCircularity, or kCylindricity no datum identifiers are needed and the datum arguments will be ignored.   This is an optional argument whose default value is null. |
| PrimaryDatumModifier | [GDTSymbolEnum](../GDTSymbolEnum.md) | Optional input GDTSymbolEnum enum value that specifies the material condition symbol to append to the primary datum. For example, the **m** symbol is used to specify maximum material condition. The PrimaryDatumIdentifier argument must be specified for this argument to be used.   This is an optional argument whose default value is 104193. |
| SecondaryDatumIdentifier | Variant | Optional input ModelDatumIdentifier object that specifies the secondary datum reference. The first datum identifier must be specified before the secondary will be used.   This is an optional argument whose default value is null. |
| SecondaryDatumModifier | [GDTSymbolEnum](../GDTSymbolEnum.md) | Optional input GDTSymbolEnum enum value that specifies the material condition symbol to append to the secondary datum. For example, the **m** symbol is used to specify maximum material condition. The SecondaryDatumIdentifier argument must be specified for this argument to be used.   This is an optional argument whose default value is 104193. |
| TertiaryDatumIdentifier | Variant | Optional input ModelDatumIdentifier object that specifies the tertiary datum reference. The first and second datum identifiers must be specified before the tertiary will be used.   This is an optional argument whose default value is null. |
| TertiaryDatumModifier | [GDTSymbolEnum](../GDTSymbolEnum.md) | Optional input GDTSymbolEnum enum value that specifies the material condition symbol to append to the tertiary datum. For example, the **m** symbol is used to specify maximum material condition. The TertiaryDatumIdentifier argument must be specified for this argument to be used.   This is an optional argument whose default value is 104193. |

## Version

Introduced in version 2015
