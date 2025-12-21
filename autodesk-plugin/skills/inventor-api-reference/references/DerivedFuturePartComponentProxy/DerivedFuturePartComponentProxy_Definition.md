# DerivedFuturePartComponentProxy.Definition Property

Parent Object: [DerivedFuturePartComponentProxy](../DerivedFuturePartComponentProxy/DerivedFuturePartComponentProxy.md)

## Description

Read-write property that returns the derived future part definition that defines the current state of the derived part.
The state of the derived part can be changed by modifying the values of the returned descriptor and assigning it back to the derived future part using the DerivedFuturePartDefinition property. The part will be updated as a result of the assignment.
Note: Definition property will return Nothing if the link to the base part is broken or if the link to the base part could not be resolved.

## Syntax

DerivedFuturePartComponentProxy.**Definition**() As [DerivedFuturePartDefinition](../DerivedFuturePartDefinition/DerivedFuturePartDefinition.md)

## Property Value

This is a read/write property whose value is a [DerivedFuturePartDefinition](../DerivedFuturePartDefinition/DerivedFuturePartDefinition.md).

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |