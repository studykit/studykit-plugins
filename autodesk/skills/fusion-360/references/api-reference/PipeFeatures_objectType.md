# PipeFeatures.objectType Property

Parent Object: [PipeFeatures](PipeFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeatures.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeatures\_var" is a variable referencing a PipeFeatures object.  ```` ``` # Get the value of the property. propertyValue = pipeFeatures_var.objectType ``` ```` |

"pipeFeatures\_var" is a variable referencing a PipeFeatures object. ```` ``` #include <Fusion/Features/PipeFeatures.h>  // Get the value of the property. string propertyValue = pipeFeatures_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |