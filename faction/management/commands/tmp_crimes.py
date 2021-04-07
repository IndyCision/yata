"""
Copyright 2019 kivou.2000607@gmail.com

This file is part of yata.

    yata is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    yata is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with yata. If not, see <https://www.gnu.org/licenses/>.
"""

from django.core.management.base import BaseCommand
from django.utils import timezone

from faction.models import Faction
from faction.models import Crimes
from yata.handy import logdate
import json

class Command(BaseCommand):
    def handle(self, **options):
        print(f"[CRON {logdate()}] START factions")
        all = Crimes.objects.all()
        n = all.count()
        for i, c in enumerate(all):
            try:
                json.loads(c.participants)
            except:
                print(f'{i+1}/{n} error {c.participants}')
                c.delete()


        print(f"[CRON {logdate()}] END")
