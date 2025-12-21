# ModelLeaderNotes Object

## Description

The ModelLeaderNotes collection object provides access to all of the leader notes in a part or assembly and provides functionality to create new leader notes.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ModelLeaderNotes/ModelLeaderNotes_Add.md) | Method that creates a leader note. |
| [CreateDefinition](../ModelLeaderNotes/ModelLeaderNotes_CreateDefinition.md) | Method that creates a leader note definition. This is a not a leader note but an object that encapsulates all of the information that defines a leader note. You use the methods and properties of this object to define the leader note you want to create and then provide it as input to the Add method. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelLeaderNotes/ModelLeaderNotes_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Count](../ModelLeaderNotes/ModelLeaderNotes_Count.md) | Property that returns the number of items in this collection. |
| [Item](../ModelLeaderNotes/ModelLeaderNotes_Item.md) | Property that returns an item from the collection. You can provide either the index of the item in the collection, where the first item is index 1, or you can provide the name of the object. |
| [Type](../ModelLeaderNotes/ModelLeaderNotes_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelAnnotations.ModelLeaderNotes](../ModelAnnotations/ModelAnnotations_ModelLeaderNotes.md)

## Version

Introduced in version 2018
