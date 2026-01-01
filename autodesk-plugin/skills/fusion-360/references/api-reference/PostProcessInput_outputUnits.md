# PostProcessInput.outputUnits Property

Parent Object: [PostProcessInput](PostProcessInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/PostProcessInput.h>

## Description

Gets and sets the units option for the CNC output. Valid options are DocumentUnitsOutput, InchesOutput or MillimetersOutput

## Syntax

* [Python](#Python)
* [C++](#C++)

"postProcessInput\_var" is a variable referencing a PostProcessInput object. |

"postProcessInput\_var" is a variable referencing a PostProcessInput object. ```` ``` #include <Cam/CAM/PostProcessInput.h>  // Get the value of the property. PostOutputUnitOptions propertyValue = postProcessInput_var->outputUnits();  // Set the value of the property, where value_var is a PostOutputUnitOptions. bool returnValue = postProcessInput_var->outputUnits(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PostOutputUnitOptions](PostOutputUnitOptions.htm).

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |