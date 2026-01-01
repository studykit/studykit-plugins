# Application.activeProduct Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the current active product.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<Product> propertyValue = application_var->activeProduct(); ``` ```` |

## Property Value

This is a read only property whose value is a [Product](Product.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |