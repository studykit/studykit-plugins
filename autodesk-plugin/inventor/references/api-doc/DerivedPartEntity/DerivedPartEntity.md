# DerivedPartEntity Object

## Description

The DerivedPartEntity object contains the information associated with an entity being derived.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedPartEntity/DerivedPartEntity_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DeriveStatus](../DerivedPartEntity/DerivedPartEntity_DeriveStatus.md) | Read-write property that gets and sets the derive status for this entity. |
| [ReferencedEntity](../DerivedPartEntity/DerivedPartEntity_ReferencedEntity.md) | Property that returns the entity in the part document. This can be used to perform additional queries to help to determine whether to include this entity or not. |
| [Type](../DerivedPartEntity/DerivedPartEntity_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedPartEntities.Item](../DerivedPartEntities/DerivedPartEntities_Item.md)

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |