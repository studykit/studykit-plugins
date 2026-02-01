# NCProgram.generatedDataCollection Property

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a NCProgram object. |

"nCProgram\_var" is a variable referencing a NCProgram object. ```` ``` #include <Cam/NCProgram/NCProgram.h>  // Get the value of the property. Ptr<GeneratedDataCollection> propertyValue = nCProgram_var->generatedDataCollection(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeneratedDataCollection](GeneratedDataCollection.htm).

## Version

Introduced in version July 2023

---

|  |  |
| --- | --- |
| Â© Copyright 2025 Autodesk, Inc. | Comment on this page. |