# Sketch.isComputeDeferred Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

This property temporarily turns off sketch computing. It is used to increase the performance as sketch geometry is created and modified. Once the sketch is drawn, this property should be set to false to allow the sketch to recompute. The file does not save this setting and is always false when a file is opened.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object.  ```` ``` # Get the value of the property. propertyValue = sketch_var.isComputeDeferred  # Set the value of the property. sketch_var.isComputeDeferred = propertyValue ``` ```` |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. boolean propertyValue = sketch_var->isComputeDeferred();  // Set the value of the property, where value_var is a boolean. bool returnValue = sketch_var->isComputeDeferred(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |