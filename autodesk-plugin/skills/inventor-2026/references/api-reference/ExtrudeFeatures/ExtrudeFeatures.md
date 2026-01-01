# ExtrudeFeatures Object

## Description

The ExtrudeFeatures collection object provides access to all of the ExtrudeFeature object in a part component definition and provides methods to create additional ExtrudeFeatures.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ExtrudeFeatures/ExtrudeFeatures_Add.md) | Method that creates a new Extrude feature. |
| [CreateExtrudeDefinition](../ExtrudeFeatures/ExtrudeFeatures_CreateExtrudeDefinition.md) | Method that creates a new ExtrudeDefinition object. The object created does not represent an extrude feature but instead is a representation of the information that defines an extrude feature. You can use this object as input to the ExtrudeFeatures.Add method to create the actual feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ExtrudeFeatures/ExtrudeFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ExtrudeFeatures/ExtrudeFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ExtrudeFeatures/ExtrudeFeatures_Item.md) | Returns the specified object from the collection. |
| [Type](../ExtrudeFeatures/ExtrudeFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Features.ExtrudeFeatures](../Features/Features_ExtrudeFeatures.md), [FlatPatternFeatures.ExtrudeFeatures](../FlatPatternFeatures/FlatPatternFeatures_ExtrudeFeatures.md), [PartFeatures.ExtrudeFeatures](../PartFeatures/PartFeatures_ExtrudeFeatures.md), [SheetMetalFeatures.ExtrudeFeatures](../SheetMetalFeatures/SheetMetalFeatures_ExtrudeFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create and Edit an Extrude Feature with a pocket](../../sample-programs/PartFeature_SetEndOfPart_Sample.md) | This sample demonstrates how to edit an extrude feature. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5
