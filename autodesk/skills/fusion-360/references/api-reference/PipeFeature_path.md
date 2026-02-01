# PipeFeature.path Property

Parent Object: [PipeFeature](PipeFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PipeFeature.h>

## Description

Gets and sets the path to create the Pipe. This property returns null in the case where the feature is non-parametric. The path can be either closed (you can reach again the starting point by following the curves) or open (the starting point and end point are different in the path).

## Syntax

* [Python](#Python)
* [C++](#C++)

"pipeFeature\_var" is a variable referencing a PipeFeature object.  ```` ``` # Get the value of the property. propertyValue = pipeFeature_var.path  # Set the value of the property. pipeFeature_var.path = propertyValue ``` ```` |

"pipeFeature\_var" is a variable referencing a PipeFeature object. ```` ``` #include <Fusion/Features/PipeFeature.h>  // Get the value of the property. Ptr<Path> propertyValue = pipeFeature_var->path();  // Set the value of the property, where value_var is a Path. bool returnValue = pipeFeature_var->path(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Path](Path.htm).

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |