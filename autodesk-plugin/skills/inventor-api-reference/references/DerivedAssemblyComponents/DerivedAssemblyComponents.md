# DerivedAssemblyComponents Object

## Description

The DerivedAssemblyComponents collection object provides access to all of the existing objects in a part and provides methods to create additional derived assembly components.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../DerivedAssemblyComponents/DerivedAssemblyComponents_Add.md) | Method that creates a new using the information supplied by the input DerivedAssemblyDefinition object. If successful, the new DerivedAssemblyComponent is returned. |
| [CreateDefinition](../DerivedAssemblyComponents/DerivedAssemblyComponents_CreateDefinition.md) | Method that creates a new Definition. The returned definition provides access to all of the items in the document that can be derived. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DerivedAssemblyComponents/DerivedAssemblyComponents_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../DerivedAssemblyComponents/DerivedAssemblyComponents_Count.md) | Property that returns the number of items in the collection. |
| [Item](../DerivedAssemblyComponents/DerivedAssemblyComponents_Item.md) | Returns the specified object from the collection. |
| [Parent](../DerivedAssemblyComponents/DerivedAssemblyComponents_Parent.md) | Property that returns the parent ComponentDefinition object. |
| [Type](../DerivedAssemblyComponents/DerivedAssemblyComponents_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ReferenceComponents.DerivedAssemblyComponents](../ReferenceComponents/ReferenceComponents_DerivedAssemblyComponents.md)

## Version

Introduced in version 5.3
