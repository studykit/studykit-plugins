# TableParameter.ModelValue Property

Parent Object: [TableParameter](../TableParameter/TableParameter.md)

## Description

Property that returns the evaluation of this parameter (in database units) that is currently used by the model. This takes into account the value computed from the expression and the tolerance. This method is only valid for numeric unit types and will fail for Text and Boolean unit types.

## Syntax

TableParameter.**ModelValue**() As Double

## Property Value

This is a read only property whose value is a Double.

## Version

Introduced in version 6
