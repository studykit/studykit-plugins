# DerivedFutureAssemblyComponent.Definition Property

Parent Object: [DerivedFutureAssemblyComponent](../DerivedFutureAssemblyComponent/DerivedFutureAssemblyComponent.md)

## Description

Read-write property that returns the derived future assembly definition that defines the current state of the derived future assembly.

The state of the derived future assembly can be changed by modifying the values of the returned descriptor and assigning it back to the derived future assembly using the DerivedFutureAssemblyDefinition property. The part will be updated as a result of the assignment.
Note: Definition property will return Nothing if the link to the base assembly is broken or if the link to the base assembly could not be resolved.

## Syntax

DerivedFutureAssemblyComponent.**Definition**() As [DerivedFutureAssemblyDefinition](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition.md)

## Property Value

This is a read/write property whose value is a [DerivedFutureAssemblyDefinition](../DerivedFutureAssemblyDefinition/DerivedFutureAssemblyDefinition.md).

## Version

Introduced in version 2018
