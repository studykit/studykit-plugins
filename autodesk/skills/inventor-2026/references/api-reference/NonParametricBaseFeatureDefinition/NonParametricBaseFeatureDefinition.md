# NonParametricBaseFeatureDefinition Object

## Description

The NonParametricBaseFeatureDefinition is a utility object used for creating, querying, and editing non-parametric base features. A NonParametricBaseFeatureDefinition object can be created using the CreateDefinition method of the NonParametricBaseFeatures collection object. They can also be obtained from existing NonParametricBaseFeature objects.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [BRepEntities](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition_BRepEntities.md) | Read-write property that defines the geometry to be used for creating the non-parametric base feature. |
| [DeleteOriginal](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition_DeleteOriginal.md) | Read-write property that defines if the original geometry in the construction environment is deleted. |
| [IsAssociative](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition_IsAssociative.md) | Read-write property that defines if the copied geometry should be associative to the original geometry. |
| [OutputType](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition_OutputType.md) | Read-write property that specifies the desired result type. |
| [TargetOccurrence](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition_TargetOccurrence.md) | Read-write property that specifies the desired target Occurrence. |

## Accessed From

[NonParametricBaseFeatures.CreateDefinition](../NonParametricBaseFeatures/NonParametricBaseFeatures_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011
