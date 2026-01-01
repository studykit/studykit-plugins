# PostProcessInput.postProperties Property

Parent Object: [PostProcessInput](PostProcessInput.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/PostProcessInput.h>

## Description

Gets and sets the list of post properties. Each property has a string name and a ValueInput object. The default value for this is an empty NamedValues.

## Syntax

* [Python](#Python)
* [C++](#C++)

"postProcessInput\_var" is a variable referencing a PostProcessInput object. |

"postProcessInput\_var" is a variable referencing a PostProcessInput object. ```` ``` #include <Cam/CAM/PostProcessInput.h>  // Get the value of the property. Ptr<NamedValues> propertyValue = postProcessInput_var->postProperties();  // Set the value of the property, where value_var is a NamedValues. bool returnValue = postProcessInput_var->postProperties(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [NamedValues](NamedValues.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Post Toolpaths API Sample](PostToolpaths_Sample_Sample.htm) | Demonstrates posting toolpaths in the active document. |

## Version

Introduced in version May 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |