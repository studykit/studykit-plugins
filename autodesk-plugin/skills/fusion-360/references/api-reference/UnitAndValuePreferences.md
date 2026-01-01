# UnitAndValuePreferences Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Application/UnitAndValuePreferences.h>

## Description

The UnitAndValuePreferences object provides access to unit and value precision related preferences.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](UnitAndValuePreferences_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angularPrecision](UnitAndValuePreferences_angularPrecision.htm) | Gets and sets the angular precision. This value specifies the number of decimals to display. |
| [areAbbreviationsForUnitDisplayed](UnitAndValuePreferences_areAbbreviationsForUnitDisplayed.htm) | Gets and sets if abbreviations are used for units display. |
| [areSymbolsForUnitDisplayed](UnitAndValuePreferences_areSymbolsForUnitDisplayed.htm) | Gets and sets if symbols are used for units display. |
| [areTrailingZerosHidden](UnitAndValuePreferences_areTrailingZerosHidden.htm) | Gets and sets if trailing zeros are hidden when displaying numbers. |
| [degreeDisplayFormat](UnitAndValuePreferences_degreeDisplayFormat.htm) | Gets and sets the degree display format. |
| [footAndInchDisplayFormat](UnitAndValuePreferences_footAndInchDisplayFormat.htm) | Gets and sets the foot and inch display format. |
| [generalPrecision](UnitAndValuePreferences_generalPrecision.htm) | Gets and sets the general precision for distance values. This value specifies the number of decimals to display. |
| [isPeriodDecimalPoint](UnitAndValuePreferences_isPeriodDecimalPoint.htm) | Gets and sets if the decimal is a period or comma. |
| [isScientificNotationUsed](UnitAndValuePreferences_isScientificNotationUsed.htm) | Gets and sets if scientific notation is used when displaying numbers. |
| [isValid](UnitAndValuePreferences_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [materialDisplayUnit](UnitAndValuePreferences_materialDisplayUnit.htm) | Gets and sets the units types to use when displaying values. |
| [minimumPrecisionWhenHidingZeros](UnitAndValuePreferences_minimumPrecisionWhenHidingZeros.htm) | Gets and sets the minimum number of digits to the right of the decimal to display before hiding trailing zeros. |
| [objectType](UnitAndValuePreferences_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [scientificNotationPrecision](UnitAndValuePreferences_scientificNotationPrecision.htm) | Gets and sets the number scientific notation precision. This value specifies the number of decimals to display. |
| [useScientficNotationAbove](UnitAndValuePreferences_useScientficNotationAbove.htm) | Gets and sets the number of whole digits that will be displayed before switching to scientific notation. |
| [useScientficNotationBelow](UnitAndValuePreferences_useScientficNotationBelow.htm) | Gets and sets the number of non zero decimal places that will be displayed before switching to scientific notation. |

## Accessed From

[Preferences.unitAndValuePreferences](Preferences_unitAndValuePreferences.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |