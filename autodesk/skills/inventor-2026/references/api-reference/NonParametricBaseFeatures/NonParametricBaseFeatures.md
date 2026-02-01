# NonParametricBaseFeatures Object

## Description

The object represented the base solid that was created when a file was imported into Autodesk Inventor.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../NonParametricBaseFeatures/NonParametricBaseFeatures_Add.md) | Method that adds a NonParametricBaseFeature to the collection. |
| [AddByDefinition](../NonParametricBaseFeatures/NonParametricBaseFeatures_AddByDefinition.md) | Method that creates a new NonParametricBaseFeature object. |
| [CreateDefinition](../NonParametricBaseFeatures/NonParametricBaseFeatures_CreateDefinition.md) | Method that creates and returns a NonParametricBaseFeatureDefinition object. This object is not a non-parametric base feature but contains the information that defines one and be used to create a new non-parametric base feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../NonParametricBaseFeatures/NonParametricBaseFeatures_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../NonParametricBaseFeatures/NonParametricBaseFeatures_Count.md) | Property that returns the number of items in this collection. |
| [Item](../NonParametricBaseFeatures/NonParametricBaseFeatures_Item.md) | Returns the specified NonParametricBaseFeature object from the collection. |
| [Type](../NonParametricBaseFeatures/NonParametricBaseFeatures_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PartFeatures.NonParametricBaseFeatures](../PartFeatures/PartFeatures_NonParametricBaseFeatures.md), [SheetMetalFeatures.NonParametricBaseFeatures](../SheetMetalFeatures/SheetMetalFeatures_NonParametricBaseFeatures.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |
| [Imprint bodies within an assembly.](../../sample-programs/ImprintUsingOccurrences_Sample.md) | This sample demonstrates creating imprinted bodies from two selected occurrences in an assembly. |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Create primitive BRep](../../sample-programs/TransientBRep_Sample.md) | This sample demonstrates the creation of primitive (solid) BRep. |

## Version

Introduced in version 6
