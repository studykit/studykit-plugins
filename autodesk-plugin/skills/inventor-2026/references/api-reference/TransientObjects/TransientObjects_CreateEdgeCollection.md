# TransientObjects.CreateEdgeCollection Method

Parent Object: [TransientObjects](../TransientObjects/TransientObjects.md)

## Description

Method creates a new EdgeCollection object. Optionally, the resulting EdgeCollection can be initialized with the contents of an enumerator containing edges that is passed in. Typically, an empty EdgeCollection will be created and populated using the Add method of the EdgeCollection object.

## Syntax

TransientObjects.**CreateEdgeCollection**( [***ObjectsEnumerator***] As Variant ) As [EdgeCollection](../EdgeCollection/EdgeCollection.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ObjectsEnumerator | Variant | Input enumerator object that contains edges. For example, the Edges object returned by the Edges property of a face can be used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |
| [Creating flange features](../../sample-programs/FlangeDefinition_SetOffsetWidthExtent_Sample.md) | Demonstrates creating flange features of various width extents. This creates a new document, creates a face feature and adds a flange feature on four edges. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |

## Version

Introduced in version 5.3
