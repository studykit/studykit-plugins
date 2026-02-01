# FeatureControlFrameRows.Add Method

Parent Object: [FeatureControlFrameRows](../FeatureControlFrameRows/FeatureControlFrameRows.md)

## Description

Method that adds a row to the feature control frame.

## Syntax

FeatureControlFrameRows.**Add**( ***GeometricCharacteristic*** As [GeometricCharacteristicEnum](../GeometricCharacteristicEnum.md), ***Tolerance*** As String, [***LowerTolerance***] As String, [***DatumOne***] As String, [***DatumTwo***] As String, [***DatumThree***] As String ) As [FeatureControlFrameRow](../FeatureControlFrameRow/FeatureControlFrameRow.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| GeometricCharacteristic | [GeometricCharacteristicEnum](../GeometricCharacteristicEnum.md) | Input GeometricCharacteristicEnum that specifies the geometric characteristic symbol for the row. |
| Tolerance | String | Input String that specifies the tolerance associated with this geometric characteristic. The string can contain symbols specified using the StyleOverride tag. Input String that specifies the tolerance associated with this geometric characteristic. The string can contain symbols specified using the StyleOverride tag. For example, use `"<StyleOverride Font='AIGDT'\>m</StyleOverride>"` to specify ![](../images/styleoverride_aigdt_m.png). |
| LowerTolerance | String | Optional input String that specifies the lower tolerance associated with this geometric characteristic. Applies to ANSI standard only. The string can contain symbols specified using the StyleOverride tag. For example, use `"<StyleOverride Font='AIGDT'\>m</StyleOverride>"` to specify ![](../images/styleoverride_aigdt_m.png). |
| DatumOne | String | Optional input String that specifies the first datum that affects the tolerance. The string can contain symbols specified using the StyleOverride tag. For example, use `"<StyleOverride Font='AIGDT'\>m</StyleOverride>"` to specify ![](../images/styleoverride_aigdt_m.png).   This is an optional argument whose default value is "". |
| DatumTwo | String | Optional input String that specifies the second datum that affects the tolerance. The string can contain symbols specified using the StyleOverride tag. For example, use `"<StyleOverride Font='AIGDT'\>m</StyleOverride>"` to specify ![](../images/styleoverride_aigdt_m.png).   This is an optional argument whose default value is "". |
| DatumThree | String | Optional input String that specifies the third datum that affects the tolerance. The string can contain symbols specified using the StyleOverride tag. For example, use `"<StyleOverride Font='AIGDT'\>m</StyleOverride>"` to specify ![](../images/styleoverride_aigdt_m.png).   This is an optional argument whose default value is "". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding and editing a feature control frame](../../sample-programs/FeatureControlFrame_FeatureControlFrameRows_Sample.md) | These samples demonstrate editing an existing feature control frame symbol. The first sample adds a row to an existing symbol. The second sample replaces all rows of an existing symbol. |
| [Create a feature control frame symbol](../../sample-programs/FeatureControlFrames_Add_Sample.md) | This sample demonstrates the creation of a feature control frame symbol. |

## Version

Introduced in version 2009
