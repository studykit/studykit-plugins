# FinishDefinition Object

## Description

The FinishDefinition object represents all of the information that defines a finish feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../FinishDefinition/FinishDefinition_Copy.md) | Method that creates a copy of this FinishDefinition object. |
| [DisableProperties](../FinishDefinition/FinishDefinition_DisableProperties.md) | Method that disables or enables the properties in this finish definition. |
| [IsPropertyDisabled](../FinishDefinition/FinishDefinition_IsPropertyDisabled.md) | Method that returns whether the specified property is disabled or not. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Appearance](../FinishDefinition/FinishDefinition_Appearance.md) | Read-write property that gets and sets the appearance for the finish feature. |
| [Application](../FinishDefinition/FinishDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Comment](../FinishDefinition/FinishDefinition_Comment.md) | Read-write property that gets and sets the comment for the finish feature. |
| [Depth](../FinishDefinition/FinishDefinition_Depth.md) | Read-write property that provides access to the depth of the feature. |
| [Description](../FinishDefinition/FinishDefinition_Description.md) | Read-write property that gets and sets the description for the finish feature. |
| [ExcludedEntities](../FinishDefinition/FinishDefinition_ExcludedEntities.md) | Read-write property that gets and sets the Face objects and their proxies that will be excluded from the finish feature. Valid objects in the ObjectCollection can be Face objects and the proxies. |
| [FinishType](../FinishDefinition/FinishDefinition_FinishType.md) | Read-write property that gets and sets the finish type for the finish feature. |
| [Hardness](../FinishDefinition/FinishDefinition_Hardness.md) | Read-write property that provides access to the hardness of the feature. |
| [IncludedEntities](../FinishDefinition/FinishDefinition_IncludedEntities.md) | Read-write property that gets and sets the Face and SurfaceBody objects and their proxies on which the finish feature is created. Valid objects in the ObjectCollection can be Face, SurfaceBody and the proxies, or FaceCollection that contains Face or FaceProxy. |
| [Parent](../FinishDefinition/FinishDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ProcessName](../FinishDefinition/FinishDefinition_ProcessName.md) | Read-write property that gets and sets the process name for the finish feature. |
| [ShortDescription](../FinishDefinition/FinishDefinition_ShortDescription.md) | Read-write property that gets and sets the short description for the finish feature. |
| [Thickness](../FinishDefinition/FinishDefinition_Thickness.md) | Read-write property that provides access to the thickness of the feature. |
| [Type](../FinishDefinition/FinishDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[FinishDefinition.Copy](../FinishDefinition/FinishDefinition_Copy.md), [FinishFeature.Definition](../FinishFeature/FinishFeature_Definition.md), [FinishFeatureProxy.Definition](../FinishFeatureProxy/FinishFeatureProxy_Definition.md), [FinishFeatures.CreateDefinition](../FinishFeatures/FinishFeatures_CreateDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Finish Feature Creation](../../sample-programs/FinishFeatureCreation_Sample.md) | This sample demonstrates how to create a finish feature. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |