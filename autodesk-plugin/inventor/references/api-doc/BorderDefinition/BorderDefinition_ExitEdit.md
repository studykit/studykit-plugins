# BorderDefinition.ExitEdit Method

Parent Object: [BorderDefinition](../BorderDefinition/BorderDefinition.md)

## Description

Method that closes the currently active sketch (see below for limitations) and depending on the input parameters, replaces the sketch of the border definition with the edited sketch.

## Remarks

You can also choose to create a new border definition using the edited sketch or close the edited sketch without saving any changes. This method is only valid to be called when a sketch associated with a BorderDefinition object has been opened for edit using the Edit method of the BorderDefinition object, otherwise an error will occur.

## Syntax

BorderDefinition.**ExitEdit**( [***SaveChanges***] As Boolean, [***SaveAsName***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SaveChanges | Boolean | Input Boolean that specifies whether to save the changes or not. True indicates to save the changes. Setting this property to False will cause the sketch to close and lose all edits. |
| SaveAsName | Variant | Input String that specifies the name of the new border definition to create. This argument is used in the case where the SaveChanges argument is True. If not specified, or an empty string is supplied, the edited sketch replaces the sketch associated with the border definition being edited. If a string is supplied, a new border definition is created and the edited sketch is used for it. The supplied name must be unique with respect to all other objects in the document.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |