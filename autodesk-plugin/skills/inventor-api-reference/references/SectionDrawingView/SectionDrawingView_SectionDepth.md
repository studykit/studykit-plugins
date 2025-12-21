# SectionDrawingView.SectionDepth Property

Parent Object: [SectionDrawingView](../SectionDrawingView/SectionDrawingView.md)

## Description

Property that gets and sets the section depth in centimeters. Setting this property automatically toggles the FullSectionDepth property to False. Setting the property to a value between 0 and 0.00003 sets the depth to the smallest available section depth value of 0.00003. This property does not apply (and setting it returns an error) if the SliceAllParts property is set to True.

## Syntax

SectionDrawingView.**SectionDepth**() As Double

## Property Value

This is a read/write property whose value is a Double.

## Version

Introduced in version 2009
