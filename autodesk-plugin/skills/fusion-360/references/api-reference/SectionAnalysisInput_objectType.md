# SectionAnalysisInput.objectType Property

Parent Object: [SectionAnalysisInput](SectionAnalysisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysisInput.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object.  ```` ``` # Get the value of the property. propertyValue = sectionAnalysisInput_var.objectType ``` ```` |

"sectionAnalysisInput\_var" is a variable referencing a SectionAnalysisInput object. ```` ``` #include <Fusion/Fusion/SectionAnalysisInput.h>  // Get the value of the property. string propertyValue = sectionAnalysisInput_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |