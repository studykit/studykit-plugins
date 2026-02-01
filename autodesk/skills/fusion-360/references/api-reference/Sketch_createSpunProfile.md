# Sketch.createSpunProfile Method

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Creates sketch geometry that represents the spun profile. The spun profile is the silhouette of the entities as if they were spinning around an axis. The created spun profile is based on the information provided by the SpunProfileInput object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object.```` ``` returnValue = sketch_var.createSpunProfile(input) ``` ```` |

"sketch\_var" is a variable referencing a [Sketch](Sketch.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchEntity](SketchEntity.htm)[] | An array of sketch entities that were created as a result of the spun profile. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [SpunProfileInput](SpunProfileInput.htm) | The SpunProfileInput object that specifies the input needed to create the spun profile. |

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |