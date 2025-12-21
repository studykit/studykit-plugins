# PointInference Object

## Description

The PointInference object provides access to information that defines how the current point is being inferred.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../PointInference/PointInference_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Entity](../PointInference/PointInference_Entity.md) | Property that returns the object(s) that were used in defining the inference. The enumerator contains a single GeometryIntent object when a drawing document is active. |
| [InferenceType](../PointInference/PointInference_InferenceType.md) | Property that returns the type of inference. |
| [Type](../PointInference/PointInference_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[PointInferenceEnumerator.Item](../PointInferenceEnumerator/PointInferenceEnumerator_Item.md)

## Version

Introduced in version 5
