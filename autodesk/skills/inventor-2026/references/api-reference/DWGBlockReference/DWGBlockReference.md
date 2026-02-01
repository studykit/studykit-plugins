# DWGBlockReference Object

Derived from: [DWGEntity](../DWGEntity/DWGEntity.md) Object

## Description

DWGBlockReference Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetObject](../DWGBlockReference/DWGBlockReference_GetObject.md) | Method that returns the corresponding object in the block reference for the given object from its definition. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DWGBlockReference/DWGBlockReference_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Definition](../DWGBlockReference/DWGBlockReference_Definition.md) | Read-only property that returns the definition object that this DWGBlockReference is an instance of. |
| [HandleID](../DWGBlockReference/DWGBlockReference_HandleID.md) | Read-only property that returns the HandleID for the DWGEntity. |
| [Parent](../DWGBlockReference/DWGBlockReference_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [ParentEntity](../DWGBlockReference/DWGBlockReference_ParentEntity.md) | Read-only property that returns the parent DWGEntity of the entity. |
| [Transformation](../DWGBlockReference/DWGBlockReference_Transformation.md) | Read-only property that returns the transformation matrix for the DWGBlockReference instance. |
| [Type](../DWGBlockReference/DWGBlockReference_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[DWGBlockReferenceProxy.NativeObject](../DWGBlockReferenceProxy/DWGBlockReferenceProxy_NativeObject.md), [DWGBlockReferencesEnumerator.Item](../DWGBlockReferencesEnumerator/DWGBlockReferencesEnumerator_Item.md)

## Derived Classes

[DWGBlockReferenceProxy](../DWGBlockReferenceProxy/DWGBlockReferenceProxy.md)

## Version

Introduced in version 2016
