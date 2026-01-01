# SketchedSymbolDefinition.ExitEdit Method

Parent Object: [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Description

Method that closes the currently active sketch (see below for limitations) and depending on the input parameters, replaces the sketch of the sketched symbol definition with the edited sketch.

## Remarks

You can also choose to create a new sketched symbol definition using the edited sketch or close the edited sketch without saving any changes. This method is only valid to be called when a sketch associated with a SketchedSymbolDefinition object has been opened for edit using the Edit method of the SketchedSymbolDefinition object, otherwise an error will occur.

## Syntax

SketchedSymbolDefinition.**ExitEdit**( [***SaveChanges***] As Boolean, [***SaveAsName***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SaveChanges | Boolean | Input Boolean that specifies whether to save the changes or not. True indicates to save the changes. Setting this property to False will cause the sketch to close and lose all edits. |
| SaveAsName | Variant | Input String that specifies the name of the new sketched symbol definition to create. This argument is used in the case where the SaveChanges argument is True. If not specified, or an empty string is supplied, the edited sketch replaces the sketch associated with the sketched symbol definition being edited. If a string is supplied, a new sketched symbol definition is created and the edited sketch is used for it. The supplied name must be unique with respect to all other SketchedSymbolDefinition objects in the document.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |

## Version

Introduced in version 5.3
