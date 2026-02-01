# BreakOperation.AllAffectedViews Property

Parent Object: [BreakOperation](../BreakOperation/BreakOperation.md)

## Description

Property that returns all the DrawingView objects affected by this break operation. Multiple drawing views can be affected by a break operation if children views inherit breaks or if the break is propagated up to the parent view.

## Syntax

BreakOperation.**AllAffectedViews**() As [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md)

## Property Value

This is a read only property whose value is an [ObjectsEnumerator](../ObjectsEnumerator/ObjectsEnumerator.md).

## Version

Introduced in version 2010
