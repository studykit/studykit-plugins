# ModelHoleThreadNotes Object

## Description

The ModelHoleThreadNotes collection object provides access to all of the hole and thread notes in a part or assembly and provides functionality to create new hole and thread notes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ModelHoleThreadNotes/ModelHoleThreadNotes_Add.md) | Method that creates a thread or hole note. |
| [CreateClearanceInfo](../ModelHoleThreadNotes/ModelHoleThreadNotes_CreateClearanceInfo.md) | Method that creates a new HoleClearanceInfo object that can be used in editing HoleFeature objects. |
| [CreateDefinition](../ModelHoleThreadNotes/ModelHoleThreadNotes_CreateDefinition.md) | Method that creates a hole or thread note definition. This is a not a hole or thread note but an object that encapsulates all of the information that defines a hole or thread note. You use the methods and properties of this object to define the hole or thread note you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelHoleThreadNotes/ModelHoleThreadNotes_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../ModelHoleThreadNotes/ModelHoleThreadNotes_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ModelHoleThreadNotes/ModelHoleThreadNotes_Item.md) | Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object. |
| [Type](../ModelHoleThreadNotes/ModelHoleThreadNotes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelAnnotations.ModelHoleThreadNotes](../ModelAnnotations/ModelAnnotations_ModelHoleThreadNotes.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |