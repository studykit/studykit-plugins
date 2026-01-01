# DriveSettings.IsInitialized Property

Parent Object: [DriveSettings](../DriveSettings/DriveSettings.md)

## Description

Read-only property that returns whether the drive parameters have been set for this relationship. If this property returns False, the properties on this object will return hard-coded default values and the methods will fail. Calling properties and methods to set drive parameters will automatically toggle this property to True.

## Syntax

DriveSettings.**IsInitialized**() As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Version

Introduced in version 2014
