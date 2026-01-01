# PathPatternFeatureInput.path Property

Parent Object: [PathPatternFeatureInput](PathPatternFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/PathPatternFeatureInput.h>

## Description

Gets and sets the path to create the pattern on path.

## Syntax

* [Python](#Python)
* [C++](#C++)

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. |

"pathPatternFeatureInput\_var" is a variable referencing a PathPatternFeatureInput object. ```` ``` #include <Fusion/Features/PathPatternFeatureInput.h>  // Get the value of the property. Ptr<Path> propertyValue = pathPatternFeatureInput_var->path();  // Set the value of the property, where value_var is a Path. bool returnValue = pathPatternFeatureInput_var->path(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Path](Path.htm).

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |