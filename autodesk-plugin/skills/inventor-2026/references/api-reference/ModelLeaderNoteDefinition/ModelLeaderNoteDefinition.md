# ModelLeaderNoteDefinition Object

## Description

The ModelLeaderNoteDefinition provides access to all of the information that defines a model leader note.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Copy.md) | Method that creates a copy of this LeaderModelNoteDefinition object. The new LeaderModelNoteDefinition object is independent of any leader note. It can edited and used as input to edit an existing note or to create a new note. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the dimension. |
| [AnnotationPlaneDefinition](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the dimension. |
| [Application](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [ArrowheadType](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_ArrowheadType.md) | Read-write property that gets and sets the arrowhead type of the leader. |
| [AssociatedGeometries](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_AssociatedGeometries.md) | Read-write property that gets and sets the associated geometries. Valid geometries include faces, edges and vertices. |
| [Intent](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Intent.md) | Read-write property that gets and sets the geometric entity the note is attached to. |
| [Leader](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Leader.md) | Read-only property that returns the leader associated with the leader note. This property will return Nothing in the cases where this object is not associated with a leader. |
| [Parent](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Parent.md) | Read-only property that returns the parent model leader note that this definition is associated with. If the definition is not associated with any existing note this property will return Nothing. |
| [Position](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Position.md) | Read-write property that gets and sets the position of the note in the part or assembly. The point is projected onto the orientation plane. |
| [ShowTextBorder](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_ShowTextBorder.md) | Read-write property that gets and sets whether to show the text border or not. |
| [Text](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Text.md) | Read-only property that returns an object that controls all of the text information associated with this note. Properties on the returned ModelAnnoationText object can be edited to change the displayed text. |
| [Type](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelLeaderNote.Definition](../ModelLeaderNote/ModelLeaderNote_Definition.md), [ModelLeaderNoteDefinition.Copy](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_Copy.md), [ModelLeaderNoteProxy.Definition](../ModelLeaderNoteProxy/ModelLeaderNoteProxy_Definition.md), [ModelLeaderNotes.CreateDefinition](../ModelLeaderNotes/ModelLeaderNotes_CreateDefinition.md)

## Version

Introduced in version 2018
