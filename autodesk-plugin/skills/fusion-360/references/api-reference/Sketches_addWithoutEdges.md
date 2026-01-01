# Sketches.addWithoutEdges Method

Parent Object: [Sketches](Sketches.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

Creates a new sketch on the specified planar entity. If a BRepFace is provided, the edges of the face are not projected into the sketch so the result of creating a new sketch with this method will always be a new empty sketch.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketches\_var" is a variable referencing a [Sketches](Sketches.htm) object.  ```` ``` #include <Fusion/Sketch/Sketches.h>  // Uses no optional arguments. returnValue = sketches_var->addWithoutEdges(planarEntity);  // Uses optional arguments. returnValue = sketches_var->addWithoutEdges(planarEntity, occurrenceForCreation); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Sketch](Sketch.htm) | Returns the newly created Sketch or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | A construction plane or planar face that defines the sketch plane. |
| occurrenceForCreation | [Occurrence](Occurrence.htm) | A creation occurrence is needed if the planarEntity is in another component AND the sketch is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.   This is an optional argument whose default value is null. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |