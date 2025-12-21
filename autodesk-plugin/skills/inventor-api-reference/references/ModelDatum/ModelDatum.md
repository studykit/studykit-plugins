# ModelDatum Object

## Description

ModelDatum Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelDatum/ModelDatum_Delete.md) | Deletes this object. |
| [GetReferenceKey](../ModelDatum/ModelDatum_GetReferenceKey.md) | Generate the sequence of bytes, called this object's reference key, which can be held onto beyond document edits and which will allow the caller to be bound back to the live object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelDatum/ModelDatum_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelDatum/ModelDatum_AttributeSets.md) | Gets the Attribute Sets collection on this object. |
| [Definition](../ModelDatum/ModelDatum_Definition.md) | Gets and sets the ModelDatumDefinition associated with this ModelDatum object. |
| [HealthStatus](../ModelDatum/ModelDatum_HealthStatus.md) | Returns the current health status of the model datum. |
| [ModelDatumTargets](../ModelDatum/ModelDatum_ModelDatumTargets.md) | Returns a ModelDatumTargets collection object providing access to the existing model datum targets in this model datum. |
| [Name](../ModelDatum/ModelDatum_Name.md) | Gets or sets the name of this object. |
| [Parent](../ModelDatum/ModelDatum_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Type](../ModelDatum/ModelDatum_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[ModelDatumDefinition.Parent](../ModelDatumDefinition/ModelDatumDefinition_Parent.md), [ModelDatumProxy.NativeObject](../ModelDatumProxy/ModelDatumProxy_NativeObject.md), [ModelDatums.Add](../ModelDatums/ModelDatums_Add.md), [ModelDatums.Item](../ModelDatums/ModelDatums_Item.md), [ModelDatumTarget.ModelDatum](../ModelDatumTarget/ModelDatumTarget_ModelDatum.md), [ModelDatumTargetProxy.ModelDatum](../ModelDatumTargetProxy/ModelDatumTargetProxy_ModelDatum.md)

## Derived Classes

[ModelDatumProxy](../ModelDatumProxy/ModelDatumProxy.md)

## Version

Introduced in version 2023
