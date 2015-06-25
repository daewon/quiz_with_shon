object Synap {

  def perm(ls: List[Int]): List[List[Int]] = ls match {
    case Nil => Nil
    case l if l.length == 1 => List(ls)
    case ls =>
      val zipped = ls.zipWithIndex
      zipped flatMap { case (n, i) =>
        val next = zipped filter { case (_, fi) => fi != i } map (_._1)
        perm(next) map { sub => n :: sub }
      }
  }

  def makePair(ls: List[Int]): Int = {
    val splited = (1 until ls.length map { n => ls.splitAt(n) }).view
    splited map { case (l, r) =>
      val lv = if (l(0) == 0) Int.MaxValue else l
      val rv = if (r(0) == 0) Int.MaxValue else r
      if (lv == Int.MaxValue || rv == Int.MaxValue) Int.MaxValue
      else l.mkString.toInt + r.mkString.toInt
    } min
  }

  def quiz(ls: Int*) = {
    perm(ls.toList) map { l => makePair(l) } min
  }
}
