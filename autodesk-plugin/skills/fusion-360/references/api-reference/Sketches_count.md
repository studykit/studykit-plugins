# Sketches.count Property

Parent Object: [Sketches](Sketches.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketches.h>

## Description

Returns the number of sketches in a component

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketches\_var" is a variable referencing a Sketches object. |

"sketches\_var" is a variable referencing a Sketches object. ```` ``` #include <Fusion/Sketch/Sketches.h>  // Get the value of the property. uinteger propertyValue = sketches_var->count(); ``` ```` |

## Property Value

This is a read only property whose value is a uinteger.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Empty Components](DeleteEmptyComponents_Sample.htm) | Deletes empty components from the active design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |