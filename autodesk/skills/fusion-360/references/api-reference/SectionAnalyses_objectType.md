# SectionAnalyses.objectType Property

Parent Object: [SectionAnalyses](SectionAnalyses.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalyses.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sectionAnalyses\_var" is a variable referencing a SectionAnalyses object.  ```` ``` # Get the value of the property. propertyValue = sectionAnalyses_var.objectType ``` ```` |

"sectionAnalyses\_var" is a variable referencing a SectionAnalyses object. ```` ``` #include <Fusion/Fusion/SectionAnalyses.h>  // Get the value of the property. string propertyValue = sectionAnalyses_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |