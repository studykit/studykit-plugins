# NonParametricBaseFeatureDefinition.OutputType Property

Parent Object: [NonParametricBaseFeatureDefinition](../NonParametricBaseFeatureDefinition/NonParametricBaseFeatureDefinition.md)

## Description

Read-write property that specifies the desired result type.

## Syntax

NonParametricBaseFeatureDefinition.**OutputType**() As [BaseFeatureOutputTypeEnum](../BaseFeatureOutputTypeEnum.md)

## Property Value

This is a read/write property whose value is a [BaseFeatureOutputTypeEnum](../BaseFeatureOutputTypeEnum.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |
| [Associative body copy](../../sample-programs/NonParametricBaseFeatures_AddByDefinition_Sample.md) | The following sample demonstrates copying bodies (associatively and non-associatively) across parts in an assembly. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |