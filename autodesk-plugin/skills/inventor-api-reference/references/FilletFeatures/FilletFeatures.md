# FilletFeatures Object

## Description

The FilletFeatures collection object provides access to all of the objects in a component definition and provides methods to create additional FilletFeature objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../FilletFeatures/FilletFeatures_Add.md) | Method that creates a new FilletFeature. This method may be used to create fillet features of constant radius, variable radius or a combination of constant and variable radius. Setbacks may also be specified. The new FilletFeature is returned. |
| [AddSimple](../FilletFeatures/FilletFeatures_AddSimple.md) | Method that creates a new constant radius fillet where all fillets have the same radius. For more complex fillet features, the Add method of the FilletFeatures collection can be used. |
| [CreateFilletDefinition](../FilletFeatures/FilletFeatures_CreateFilletDefinition.md) | Method that creates a new FilletDefinition object. The object returned by this method is used to define the inputs for a fillet feature and is provided as the argument to the Add method of the FilletFeatures collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../FilletFeatures/FilletFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../FilletFeatures/FilletFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../FilletFeatures/FilletFeatures_Item.md) | Returns the specified FilletFeature object from the collection. |
| [Type](../FilletFeatures/FilletFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Features.FilletFeatures](../Features/Features_FilletFeatures.md), [FlatPatternFeatures.FilletFeatures](../FlatPatternFeatures/FlatPatternFeatures_FilletFeatures.md), [PartFeatures.FilletFeatures](../PartFeatures/PartFeatures_FilletFeatures.md), [SheetMetalFeatures.FilletFeatures](../SheetMetalFeatures/SheetMetalFeatures_FilletFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Fillet Feature (Complex)](../../sample-programs/FilletFeature2_Sample.md) | This sample demonstrates creating a complex fillet. The result in this case has several different constant radii fillets and two edges that use variable radius, with one of these having a different radius defined along the edge. |

## Version

Introduced in version 5
