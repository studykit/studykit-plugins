# ShellThicknessFaceSet Object

## Description

The ShellThicknessFaceSet object provides access to the faces and their associated thickness for a shell.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ShellThicknessFaceSet/ShellThicknessFaceSet_Delete.md) | Method that deletes the face set. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ShellThicknessFaceSet/ShellThicknessFaceSet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Faces](../ShellThicknessFaceSet/ShellThicknessFaceSet_Faces.md) | Gets and sets the shell boundary relative to part face. |
| [Thickness](../ShellThicknessFaceSet/ShellThicknessFaceSet_Thickness.md) | Property that returns the parameter that controls the thickness of the faces in the face set. This property will return Nothing if the shell feature has not been created yet. |
| [Type](../ShellThicknessFaceSet/ShellThicknessFaceSet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ShellDefinition.AddThicknessFaceSet](../ShellDefinition/ShellDefinition_AddThicknessFaceSet.md), [ShellDefinition.FaceSetItem](../ShellDefinition/ShellDefinition_FaceSetItem.md)

## Version

Introduced in version 9
