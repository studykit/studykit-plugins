# TransientObjects.CreateColor Method

Parent Object: [TransientObjects](../TransientObjects/TransientObjects.md)

## Description

Method to construct a new Color object.

## Syntax

TransientObjects.**CreateColor**( ***Red*** As Byte, ***Green*** As Byte, ***Blue*** As Byte, [***Opacity***] As Double ) As [Color](../Color/Color.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Red | Byte | Input Byte that specifies the red component of the color. This value must be between 0 and 255. |
| Green | Byte | Input Byte that specifies the green component of the color. This value must be between 0 and 255. |
| Blue | Byte | Input Byte that specifies the blue component of the color. This value must be between 0 and 255. |
| Opacity | Double | Optional input Double that specifies the opacity of the color. The opacity is defined using a value between 0 and 1. A value of 0 indicates complete translucency while a value of 1 is completely opaque. If not specified this argument defaults to 1. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Interference Analysis](../../sample-programs/AssemblyComponentDefinition_AnalyzeInterference_Sample.md) | This sample demonstrates the functions used to calculate interference analysis in an assembly. |
| [Create a simple appearance.](../../sample-programs/CreateSimpleAppearance_Sample.md) | Creates a sample appearance in the active part or assembly document. |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |
| [Creating a HighlightSet](../../sample-programs/Document_CreateHighlightSet_Sample.md) | Demonstrates creating a highlight set. |
| [Highlight Feature Faces](../../sample-programs/HighlightSet_Sample.md) | This sample highlights the faces of an extrusion, revolution, or hole feature. It differentiates the faces on the start cap, end cap, and side faces by highlighting them in different colors. The HighlightFeatureFaces sub highlights the feature faces. Since the highlight set objects are declared outside of this sub, the highlighting remains after the sub has finished executing. Use the ClearHighlight sub to clear the highlighting that does so by releasing the HighlightSet objects. |

## Version

Introduced in version 8
