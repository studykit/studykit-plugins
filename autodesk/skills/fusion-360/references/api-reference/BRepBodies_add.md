# BRepBodies.add Method

Parent Object: [BRepBodies](BRepBodies.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBodies.h>

## Description

Creates a new BRepBody object. The input can be a persisted or transient BRepBody and the result is a persisted BRepBody. In a direct modeling design, the BRepBody is created within the component the BRepBodies collection was obtained from. In a parametric modeling design, the new BRepBody is created within the specified Base Feature.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBodies\_var" is a variable referencing a [BRepBodies](BRepBodies.htm) object.```` ``` # Uses no optional arguments. returnValue = bRepBodies_var.add(body)  # Uses optional arguments. returnValue = bRepBodies_var.add(body, targetBaseFeature) ``` ```` |

"bRepBodies\_var" is a variable referencing a [BRepBodies](BRepBodies.htm) object.  ```` ``` #include <Fusion/BRep/BRepBodies.h>  // Uses no optional arguments. returnValue = bRepBodies_var->add(body);  // Uses optional arguments. returnValue = bRepBodies_var->add(body, targetBaseFeature); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the newly created BRepBody or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| body | [BRepBody](BRepBody.htm) | The input BRepBody. Typically this is a transient BRepBody but that's not a requirement. In any case, there is not any association back to the original BRepBody. |
| targetBaseFeature | [BaseFeature](BaseFeature.htm) | The BaseFeature object that this BRep body will be associated with. This is an optional requirement. It is required in a parametric modeling design but is ignored in a direct modeling design.   This is an optional argument whose default value is null. |

## Version

Introduced in version May 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |