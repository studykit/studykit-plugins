# DerivedPartComponents Object

## Description

The DerivedPartComponents collection object provides access to all of the existing objects in a part and provides methods to create additional derived components.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DerivedPartComponents/DerivedPartComponents_Add.md) | Method that creates a new DerivedPartDefinition using the information supplied by the input DerivedPartDefinition object. If successful, the new DerivedPartComponent is returned. |
| [CreateCoordinateSystemDef](../DerivedPartComponents/DerivedPartComponents_CreateCoordinateSystemDef.md) | Method that creates a new DerivedPartCoordinateSystemDef object. |
| [CreateTransformDef](../DerivedPartComponents/DerivedPartComponents_CreateTransformDef.md) | Method that creates a new DerivedPartTransformDef object. |
| [CreateUniformScaleDef](../DerivedPartComponents/DerivedPartComponents_CreateUniformScaleDef.md) | Method that creates a new DerivedPartUniformScaleDef object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedPartComponents/DerivedPartComponents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DerivedPartComponents/DerivedPartComponents_Count.md) | Property that returns the number of items in the collection. |
| [Item](../DerivedPartComponents/DerivedPartComponents_Item.md) | Returns the specified DerivedPartComponent object from the collection. |
| [Parent](../DerivedPartComponents/DerivedPartComponents_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Type](../DerivedPartComponents/DerivedPartComponents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ReferenceComponents.DerivedPartComponents](../ReferenceComponents/ReferenceComponents_DerivedPartComponents.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |