# FeatureControlFrames.Add Method

Parent Object: [FeatureControlFrames](../FeatureControlFrames/FeatureControlFrames.md)

## Description

Method that creates a feature control frame symbol.

## Syntax

FeatureControlFrames.**Add**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***FeatureControlFrameRows*** As [FeatureControlFrameRows](../FeatureControlFrameRows/FeatureControlFrameRows.md), [***AllAroundSymbol***] As Boolean, [***DatumIdentifier***] As String, [***Notes***] As String, [***FeatureControlFrameStyle***] As Variant, [***Layer***] As Variant ) As [FeatureControlFrame](../FeatureControlFrame/FeatureControlFrame.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing a series of Point2d objects representing the leader originating at the symbol. The last item in the collection (even if it is the only item) can be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item, else the method will fail. |
| FeatureControlFrameRows | [FeatureControlFrameRows](../FeatureControlFrameRows/FeatureControlFrameRows.md) | Input FeatureControlFrameRows object containing the definition of the rows of the feature control frame. The FeatureControlFrameRows object is created using the CreateFeatureControlFrameRows method on the FeatureControlFrames collection object. |
| AllAroundSymbol | Boolean | Optional input Boolean that specifies whether to add the all-around indicator to the symbol. The diameter is specified in the leader style. Defaults to False. |
| DatumIdentifier | String | Optional input String that specifies a datum identifier for the feature control frame. This argument is ignored if the associated style does not allow the specification of a datum identifier. This can be checked using the FeatureControlFrameStyle.AllowDatumIdentifier property. The string can contain symbols specified using the StyleOverride tag. For instance, use 'm' to specify m.   This is an optional argument whose default value is "". |
| Notes | String | Optional input String that specifies notes for the feature control frame symbol. The string can contain symbols specified using the StyleOverride tag. For example, use `"<StyleOverride Font='AIGDT'\>m</StyleOverride>"` to specify ![](../images/styleoverride_aigdt_m.png).   This is an optional argument whose default value is "". |
| FeatureControlFrameStyle | Variant | Optional input FeatureControlFrameStyle object which specifies the feature control frame style to use for the symbol. If not specified, the style defined by the active standard is used.   This is an optional argument whose default value is null. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the symbol. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create a feature control frame symbol](../../sample-programs/FeatureControlFrames_Add_Sample.md) | This sample demonstrates the creation of a feature control frame symbol. |

## Version

Introduced in version 2009
