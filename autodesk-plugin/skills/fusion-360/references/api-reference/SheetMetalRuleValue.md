# SheetMetalRuleValue Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/SheetMetalRuleValue.h>

## Description

Used to get and set the current value of a value associated with a sheet metal rule. A value can be gotten or set using a string or a double. A string can contain equations and unit specifiers whereas a double defines the size in centimeters. In the user-interface, the user is always setting the string expression. However, when programming it is typically more convenient to set it using an explicit value. When the value is set using a double, Fusion creates an equivalent expression.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SheetMetalRuleValue_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [expression](SheetMetalRuleValue_expression.htm) | Gets and sets the expression of the sheet metal rule value. This can be an equation that includes the name "Thickness" and can also include length unit specifiers. For example, a valid expression is "Thickness / 2 + 1 mm". If no units are specified, the unit is implied and uses the units associated with the rule which can be mm or inch. For example an expression of "3" will be 3 inches if the rule units are inches or 3 mm if the rule units are millimeters. |
| [isValid](SheetMetalRuleValue_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](SheetMetalRuleValue_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [value](SheetMetalRuleValue_value.htm) | Gets and sets the value of the sheet metal rule value in centimeters. Setting this value will create a new expression that is equivalent to the new value. |

## Accessed From

[SheetMetalRule.bendRadius](SheetMetalRule_bendRadius.htm), [SheetMetalRule.gap](SheetMetalRule_gap.htm), [SheetMetalRule.reliefDepth](SheetMetalRule_reliefDepth.htm), [SheetMetalRule.reliefRemnant](SheetMetalRule_reliefRemnant.htm), [SheetMetalRule.reliefWidth](SheetMetalRule_reliefWidth.htm), [SheetMetalRule.thickness](SheetMetalRule_thickness.htm), [SheetMetalRule.threeBendReliefRadius](SheetMetalRule_threeBendReliefRadius.htm), [SheetMetalRule.twoBendReliefSize](SheetMetalRule_twoBendReliefSize.htm)

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |